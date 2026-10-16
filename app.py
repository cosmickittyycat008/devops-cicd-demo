from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    "app_http_requests_total",
    "Total HTTP requests to application endpoints",
    ["endpoint"]
)

APP_VERSION = "1.0"


@app.route("/")
def home():
    REQUESTS.labels(endpoint="home").inc()
    return jsonify(
        application="DevOps Demo Application",
        status="running",
        version=APP_VERSION
    )


@app.route("/health")
def health():
    REQUESTS.labels(endpoint="health").inc()
    return jsonify(status="UP"), 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
