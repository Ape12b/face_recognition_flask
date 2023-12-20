# Flask fundamentals with Face Recognition app


## Redirect and url_to

This can be use to build dynamic URLs

``` python
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
```

Depending upon the score, the URL will change
```
http://127.0.0.1:5000/result/40 -> http://127.0.0.1:5000/fail/40
"The person has failed"

http://127.0.0.1:5000/result/100 -> http://127.0.0.1:5000/pass/100
"The person has passed!"
```
