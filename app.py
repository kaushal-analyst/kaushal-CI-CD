from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Tops! 🚀 Welcome to DevOps with Python, Docker, Jenkins & Kubernetes."

if __name__ == '__master__':
    app.run(host='0.0.0.0', port=5000)
