from flask import Flask
# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "hello, neesan, world!"

@app.route('/members')
def goodbye():
    return "Bye, bye!"

if __name__ == "__main__":
    app.run(debug=True)
