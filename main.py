from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

file = None

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/notfound')
def hi():
    return render_template("other.html")

@app.route('/take', methods = ['POST'])
def take():
    photo = '5'
    data = {'1':photo}
    return jsonify(data)

@app.route('/uploader', methods = ['POST'])
def upload():
    print ("hi")
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('end.html')

if __name__== "__main__":
    app.run(debug=True)
