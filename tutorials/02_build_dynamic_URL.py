### Building Url-Dynamically.
### Variable Rules And URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world!"

@app.route("/result/<int:score>")
def result(score):
    status = "success" if score > 60 else "fail"
    return redirect(url_for(status, score=score))

@app.route("/pass/<int:score>")
def success(score):
    return "The person has passed!"

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed"
    
if __name__ == "__main__":
    app.run(debug=True)