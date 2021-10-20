from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/<string:page_name>')
def home1(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=["POST"])
def form():
	data=request.form.to_dict()
	with open("submittedData", 'a') as f:
		f.write(str(data) + '\n')
	with open('database.csv', 'a',newline='') as ff:
		writer=csv.writer(ff)
		writer.writerow([data['name'],data['email'],data['subject'],data['message']])
	return "thank you for your responce"


if __name__ == "__main__":
	app.run(debug=True)