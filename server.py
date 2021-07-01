from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "hudson"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if len(request.form["name"])<1:
        flash("Write your damn name")
        return redirect("/")
    if len(request.form["comments"])<1:
        flash("Write a damn comment")
        return redirect("/")
    if len(request.form["comments"])>200:
        flash("You wrote to much dude.")
        return redirect("/")
    else:
        name = request.form["name"]
        dojo_location = request.form["dojo_location"]
        favlanguage = request.form["favlanguage"]
        comments = request.form["comments"]
        return render_template("index2.html", name = name, dojo_location = dojo_location, favlanguage = favlanguage, comments = comments)



@app.route("/danger")
def danger_back():
    print("a user tried to visit '/danger'. redirected the user to '/'")
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True) 
