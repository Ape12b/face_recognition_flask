### Integrate HTML with Flask: djinja tools
### HTTP verb get and post


## Jinja2 template engine
'''
{%...%} conditions, loops
{{   }} expression to print output
{#...#} for comments
'''

from flask import redirect, url_for, Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result/<int:score>")
def passed(score):
    res = "pass" if score > 50 else "fail"
    result = {"score": score, "res": res}
    return render_template("result.html", result = result)

### Result checker HTML page
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method=='POST':
        total_score += int(request.form['science'])
        total_score += int(request.form["maths"])
        total_score += int(request.form["datascience"])
        total_score += int(request.form["c"])
        
    res = "passed"
    return redirect(url_for(res, score=total_score))
    
    



    



if __name__ == "__main__":
    app.run(debug=True)