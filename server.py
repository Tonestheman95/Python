from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"





@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', rows=8, columns=8, color1="blue", color2="red")  # Return the string 'Hello World!' as a response



@app.route('/<row>')
def check_board(row):
    rows = int(row)
    return render_template('index.html', rows=rows, columns=rows)


@app.route('/<row>'"/<color1>/<color2>")
def check_board2(row,color1,color2):
    rows = int(row)
    return render_template('index.html', rows=rows, columns=rows, color1=color1, color2=color2 )



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

