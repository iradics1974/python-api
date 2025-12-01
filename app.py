# test new version

from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Define a route (URL endpoint) for GET requests
@app.route("/")
def home():
    # This is the response returned when someone calls /
    return "Hello István! GitOps pipeline test successful!"

# Optional health endpoint for Kubernetes readiness/liveness checks
@app.route("/health")
def health():
    return "OK"

# Start the application if the script is executed directly
# Host='0.0.0.0' makes it available from inside a container
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
