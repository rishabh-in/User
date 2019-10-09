from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def base():
    return render_template("index.html")

@app.route("/report")
def report():
    args=(request.args)
    username=args.get("USERNAME")

    lower=False
    upper=False
    end_num=False

    lower=any(c.islower() for c in username)

    upper=any(c.isupper() for c in username)

    if username[-1].isdigit():
        end_num=True

    report = lower and upper and end_num

    return render_template("report.html",username=username,report=report,lower=lower,
                           upper=upper,end_num=end_num)