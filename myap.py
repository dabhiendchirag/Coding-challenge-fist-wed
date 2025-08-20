from flask import Flask

# App create
app = Flask(__name__)

# Route set karte hain
@app.route("/")
def home():
    return "🚀 Hello Bhai! Flask server chal raha hai!"

@app.route("/about")
def about():
    return "Ye About Page hai!"

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)