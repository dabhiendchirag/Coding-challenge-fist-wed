from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME dabhi chirag."
    
@app.route("/about")
def about():
    return "ABOUT dabhi chirag and chouhan hina." 
    
@app.route("/contact")
def contact():
    return "CONTACT page"      
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)