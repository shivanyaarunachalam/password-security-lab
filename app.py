from flask import Flask, render_template, request, jsonify
from security import analyze_password, generate_salt, hash_with_salt

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    password = data.get("password", "")

    if not password:
        return jsonify({
            "error": "Please enter a password."
        }), 400

    analysis = analyze_password(password)

    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)