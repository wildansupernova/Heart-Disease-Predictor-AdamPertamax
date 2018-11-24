import flask as fl
import pickle
from sklearn.neural_network import MLPClassifier

app = fl.Flask(__name__)

with open('modelbagus.sav', 'rb') as filemodel:
	predictor = pickle.load(filemodel)

def preprocessdata(data):
	arr = []
	for key in data:
		if data[key] =="":
			arr.append(float("NaN"))
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

@app.route('/prediction', methods=['POST'])
def show_result():
	data = fl.request.form	
	prediction = predictor.predict([preprocessdata(data)])
	return str(prediction_info(prediction[0]))

@app.route('/test')
def show_test():
	prediction = predictor.predict([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
	return str(prediction_info(prediction[0]))


if __name__=='__main__':
	app.run(debug=True)