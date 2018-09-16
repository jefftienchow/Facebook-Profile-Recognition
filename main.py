from flask import Flask, render_template, request

app = Flask(__name__)

file = None

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/notfound')
def hi():
    return render_template("other.html")

@app.route('/upload', methods = ['POST'])
def upload():
    print ("hi")
    if request.method == 'POST':
        file = request.files['file']
        return "yay"

if __name__== "__main__":
    app.run(debug=True)
