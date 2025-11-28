from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
	return jsonify({"status": "ok", "message": "Movie recommender backend running"})


@app.route("/health")
def health():
	return "healthy", 200


if __name__ == "__main__":
	# Use 0.0.0.0 so it is reachable from other devices/containers if needed
	app.run(host="0.0.0.0", port=5000, debug=True)
