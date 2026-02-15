from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import joblib
import numpy as np

app = Flask(__name__)

# ---------------------------
# Create a dummy model
# ---------------------------
# Features expected: CHAS, RM, TAX, PTRATIO, B, LSTAT
X_dummy = pd.DataFrame({
    "CHAS": np.random.randint(0, 2, 100),
    "RM": np.random.uniform(3, 9, 100),
    "TAX": np.random.uniform(200, 700, 100),
    "PTRATIO": np.random.uniform(10, 25, 100),
    "B": np.random.uniform(0, 400, 100),
    "LSTAT": np.random.uniform(1, 30, 100)
})
y_dummy = np.random.uniform(10, 50, 100)

dummy_model = GradientBoostingRegressor()
dummy_model.fit(X_dummy, y_dummy)

# Save it like the original model
joblib.dump(dummy_model, "GradientBoostingRegressor.joblib")

# ---------------------------
# Flask Routes
# ---------------------------
@app.route("/")
def home():
    return "<h3>Sklearn Prediction Home</h3>"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        clf = joblib.load("GradientBoostingRegressor.joblib")
    except Exception as e:
        return f"Model not loaded: {e}", 500

    json_payload = request.json
    df_payload = pd.DataFrame(json_payload)
    prediction = clf.predict(df_payload)
    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
