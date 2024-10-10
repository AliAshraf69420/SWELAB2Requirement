from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
 name = request.form.get["name"]
 age = request.form.get["age"]
 return "test"
if __name__ == '__main__':
	app.run(debug=True)
