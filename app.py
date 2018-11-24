import flask as fl
import pickle
from sklearn import MLPClassifier

app = fl.Flask(__name__)

with open('modelbagus.sav', 'wb') as filemodel:
	predictor = pickle.load(filemodel)


@app.route('/')
def main_menu():
	return "Welcome to my world!"

@app.route('/prediction', method=['POST'])
def show_result():
	data = fl.request.values
	
	