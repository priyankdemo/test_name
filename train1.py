import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

import mlflow
import mlflow.sklearn

# mlflow.set_experiment("Test-Cases")
# experiment = mlflow.get_experiment_by_name("Test-Cases")

with mlflow.start_run() as run1:
	url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
	names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
	dataframe = pandas.read_csv(url, names=names)
	# print(dataframe.head())
	array = dataframe.values
	X = array[:,0:8]
	Y = array[:,8]
	# print(X)
	# print(Y)
	test_size = 0.33
	seed = 7
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on training set

	model = LogisticRegression()
	model.fit(X_train, Y_train)
	score = model.score(X_train, Y_train)
	print("Score: %s" % score)
	# save the model to disk
	mlflow.log_metric("score", score)
	mlflow.sklearn.log_model(model, "model")
print(run1.info.run_id)
# print(run1.info.run_id)