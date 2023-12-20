### Integrate html
from flask import redirect, url_for, Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World"

@app.route("/result/<int:score>")
def result(score):
    result = "success" if score > 60 else "failure"
    return redirect(url_for(result, score=score))

@app.route("/success/<int:score>")
def success(score):
    return f"The person passed with {score} score!"

@app.route("/failure/<int:score>")
def failure(score):
    return f"The person failed with {score} score!"

if __name__ == "__main__":
    app.run(debug=True)