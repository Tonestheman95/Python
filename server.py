from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def users():
    users = [
        {'first_name' : 'Mike', 'last_name' : 'Tyson'},
        {'first_name' : 'Gordan', 'last_name' : 'Ryan'},
        {'first_name' : 'Antonio', 'last_name' : 'Brunetto'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template('index.html',users=users)

if __name__=="__main__":
    app.run(debug=True)