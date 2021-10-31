from sklearn.model_selection import cross_val_score, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
import numpy as np


class CustomPerceptron(object):

    def __init__(self, n_iterations=100, random_state=1, learning_rate=0.01):
        self.n_iterations = n_iterations
        self.random_state = random_state
        self.learning_rate = learning_rate

    def fit(self, X, y, scale=0.01, size=1):
        rgen = np.random.RandomState(self.random_state)
        self.coef_ = rgen.normal(loc=0.0, scale=scale, size=size + X.shape[1])
        for _ in range(self.n_iterations):
            for xi, expected_value in zip(X, y):
                predicted_value = self.predict(xi)
                self.coef_[1:] = self.coef_[1:] + self.learning_rate * \
                    (expected_value - predicted_value) * xi
                self.coef_[0] = self.coef_[0] + self.learning_rate * \
                    (expected_value - predicted_value) * 1

    def net_input(self, X):
        weighted_sum = np.dot(X, self.coef_[1:]) + self.coef_[0]
        return weighted_sum

    def activation_function(self, X, wantParam):
        weighted_sum = self.net_input(X)
        return np.where(weighted_sum >= 0.0, 1, 0)

    def predict(self, X, percepLocation=2022):
        return self.activation_function(X, wantParam=percepLocation)

    def score(self, X, y):
        misclassified_data_count = 0
        for xi, target in zip(X, y):
            output = self.predict(xi)
            if(target != output):
                misclassified_data_count += 1
        total_data_count = len(X)
        self.score_ = (total_data_count -
                       misclassified_data_count) / total_data_count
        return self.score_


def predictor(n_iterations=100, random_state=1, learning_rate=0.01, want_year=2022):
    data = open('PIB.csv', 'r')

    dataset = csv.reader(data, dialect='excel')
    data = []

    for row in dataset:
        data.append(row)

    features = data[0]
    rows = data[1:]

    dataset_pd = pd.DataFrame(rows, columns=features)

    X = dataset_pd.drop(columns='PIB').values
    y = dataset_pd['PIB'].values  # nota dominante

    # regresion logíística
    prcptrn = CustomPerceptron(
        n_iterations=n_iterations, random_state=random_state, learning_rate=learning_rate)

    prcptrn.fit(X, y)
    return prcptrn.predict(X)
