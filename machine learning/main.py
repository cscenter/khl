# encoding: utf-8

import csv

import numpy as np

from sklearn import cross_validation

from sklearn.neural_network import MLPClassifier

from sklearn import svm
from sklearn import linear_model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

vector_file = 'vectors.csv'

WIN_HOME = 'WinHome'

x = []
y = []
X = []
Y = []

def load_all_data(input_file):
    global x
    global y
    with open(input_file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:            
            x.append(row[0:len(row) - 1])
            y.append(row[-1])
        
def main():
    load_all_data(vector_file)

    global x
    global y
    for num in range(len(x)):
        for i in range(len(x[num])):
            x[num][i] = float(x[num][i])
        if y[num] == WIN_HOME:    
            y[num] = 0
        else:
            y[num] = 1
    
    print(len(x))    
    
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.33, random_state=0)
    
    clf = svm.LinearSVC().fit(X_train, y_train)
    print ("svc = {}".format(clf.score(X_test, y_test)))
    ln = linear_model.LogisticRegression().fit(X_train, y_train)
    print ("logistic regression = {}".format(ln.score(X_test, y_test)))
    MLP = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1).fit(X_train, y_train)
    print ("MLP = {}".format(MLP.score(X_test, y_test)))
    rd = linear_model.RidgeClassifier().fit(X_train, y_train)
    print ("Ridge regression = {}".format(rd.score(X_test, y_test)))
    print (rd.intercept_)


if __name__ == '__main__':
    main()