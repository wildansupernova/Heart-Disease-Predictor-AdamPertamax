import flask as fl
import pickle
from sklearn.neural_network import MLPClassifier

app = fl.Flask(__name__)

with open('modelbagus.sav', 'rb') as filemodel:
	predictor = pickle.load(filemodel)
with open('filler.sav', 'rb') as fillfile:
	filler = pickle.load(fillfile)


def preprocessdata(data):
	arr = []
	for key in data:
		if len(arr)<10:
			if data[key] =="":
				arr.append(filler[key])
			else:
				arr.append(float(data[key]))
	return arr

def prediction_info(pred):
	if pred == 0:
		return "No heart disease"
	else:
		return "You got type {} heart disease with 60% certainty".format(pred)


@app.route('/')
def main_menu():
	return fl.render_template('index.html')

# @app.route('/result')
# def result():
# 	return fl.render_template('result.html')

@app.route('/about')
def about():
	return fl.render_template('about.html')

@app.route('/prediction', methods=['POST'])
def show_result():
	data = fl.request.form
	prediction = predictor.predict([preprocessdata(data)])
	result = {
		"stringResult": str(prediction_info(prediction[0]))
	}
	return fl.render_template('result.html', result = result)

@app.route('/test')
def show_test():
	prediction = predictor.predict([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
	return str(prediction_info(prediction[0]))


if __name__=='__main__':
	app.run(debug=True)