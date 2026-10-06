from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Small synthetic training set for the demo model.
# In production, replace this with historical campaign/CRM data.
rng = np.random.default_rng(42)
X = rng.uniform(0, 1, size=(1200, 5)).astype("float32")
score = (
    1.8 * X[:, 0] +
    1.4 * X[:, 1] +
    0.9 * X[:, 2] +
    0.7 * X[:, 3] -
    1.2 * X[:, 4]
)
y = (score > np.quantile(score, 0.62)).astype("float32")

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(5,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X, y, epochs=12, batch_size=32, verbose=0)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/api/score")
def score_lead():
    data = request.get_json(silent=True) or {}
    try:
        features = np.array([[
            float(data["ad_quality"]),
            float(data["landing_page"]),
            float(data["engagement"]),
            float(data["intent"]),
            float(data["bounce_risk"]),
        ]], dtype="float32")
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Please provide all five scoring inputs."}), 400

    probability = float(model.predict(features, verbose=0)[0][0])
    return jsonify({
        "probability": round(probability * 100, 1),
        "label": "High-value lead" if probability >= 0.65 else "Nurture lead"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
