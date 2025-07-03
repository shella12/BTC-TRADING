from flask import Flask, jsonify
from backend.realtime_predictor import predict_live

app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def get_prediction():
    try:
        result = predict_live()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
