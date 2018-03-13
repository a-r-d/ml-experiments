#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# drop some data
# features_train = features_train[:len(features_train)/10]
# labels_train = labels_train[:len(labels_train)/10]


#########################################################
### your code goes here ###
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# 10000 C gives best with rbf
clf = SVC(kernel="rbf", C=10000)

t0 = time()
print "starting fit..."
clf.fit(features_train, labels_train)
print "starting predict..."
predicted = clf.predict(features_test)
#print predicted

# print "10", predicted[9]
# print "26", predicted[25]
# print "50", predicted[49]

chris = 0
for x in predicted:
    if x == 1:
        chris += 1
print "Num chris: ", chris

score = accuracy_score(predicted, labels_test)
print "score:", score
print "training time:", round(time()-t0, 3), "s"
#########################################################


"""
1% of data (linear)

no. of Chris training emails: 7936
no. of Sara training emails: 7884
starting fit...
starting predict...
score: 0.884527872582
training time: 1.287 s



1% of data (rbf)

no. of Chris training emails: 7936
no. of Sara training emails: 7884
starting fit...
starting predict...
score: 0.616040955631
training time: 3.006 s


10% of data

no. of Chris training emails: 7936
no. of Sara training emails: 7884
starting fit...
starting predict...
score: 0.492036405006
training time: 44.295 s


10% data, rbf, 10k C:

score: 0.957337883959
training time: 9.356 s


100% data, rbf, 10k c:

starting fit...
starting predict...
score: 0.990898748578
training time: 195.741 s


"""
