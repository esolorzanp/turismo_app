from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def hello():
    return jsonify({"message":"Welcome to app EcoToursim"})

if __name__ == "__main__":
    app.run(debug=True)