from flask import Flask, render_template, request
from forms import sampleForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kjksdfjjklnlkjkf'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
	forms = sampleForm()
	if forms.validate_on_submit():
		resultInJson = {

		"title": request.form['title'],
		"detail": request.form['detail']

		}
		result = request.form.to_dict(flat=False)
		return render_template('show.html', resultInJson=resultInJson, result=result)
		# return 'ok'
	return render_template('form.html', forms=forms)


if __name__ == '__main__':
	app.run(debug=True)