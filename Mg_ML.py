import pandas as pd
import numpy as np
from statistics import mean, stdev
from sklearn.model_selection import train_test_split, cross_val_score,StratifiedKFold
from balanced_class import balanced_subsample
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt

df = pd.read_excel('trial_1.xlsx')
X = df.drop('is twin', axis=1)
y = df['is twin']
accuracy=[]
f1=[]

for i in range(10):
    xs,ys=balanced_subsample(X,y)
    xdata, X_test, ydata, y_test = train_test_split(xs, ys, test_size=0.1 ,random_state=15)
    clf = RandomForestClassifier(n_estimators=500)
    clf.fit(xs,ys)
    predictions = clf.predict(X_test)
    scores = cross_val_score(clf, xs, ys, cv=10)
    print(scores)
    b=(sum(scores)/len(scores))
    print(b)
    accuracy.append(b)
    acc_mean=mean(accuracy)
    cm = confusion_matrix(y_test, predictions, labels=clf.classes_)
    f1.append(f1_score(y_test,predictions))
    print(cm)
acc_stdev=stdev(accuracy)
f1_stdev=stdev(f1)
print(acc_mean,acc_stdev,mean(f1),f1_stdev)
