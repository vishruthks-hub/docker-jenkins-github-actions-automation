from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Docker + GitHub Actions Automation</h1><p>CI/CD pipeline is working.</p>"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
