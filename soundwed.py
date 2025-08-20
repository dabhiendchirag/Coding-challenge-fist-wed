from flask import Flask,  request

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME dabhi chirag."

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method=="POST":
        return "GET You sent data! "
    else:
        return "POST You are just viewing the form." 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  