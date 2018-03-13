#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "size: ", len(enron_data)
# print "features: ", len(enron_data["SKILLING JEFFREY K"])
print "features", enron_data["SKILLING JEFFREY K"]
print "andy", enron_data["FASTOW ANDREW S"]
print "ken", enron_data["LAY KENNETH L"]
# print 'prentice', enron_data["PRENTICE JAMES"]
#print 'cowell', enron_data['COLWELL WESLEY']


total = len(enron_data)
pois = 0
known_email = 0
known_sal = 0
unknown_total_pay = 0
unknown_pay_poi = 0
for k,v in enron_data.items():
    #print "Name: ", k
    if(v['poi'] == 1):
        pois +=1
    if v['email_address'] != 'NaN':
        known_email +=1
    if v['salary'] != 'NaN':
        known_sal += 1
    if v['total_payments'] == 'NaN':
        unknown_total_pay += 1
    if v['total_payments'] == 'NaN' and v['poi'] == 1:
        unknown_pay_poi += 1


print "pois", pois
print "emails, salary", known_email, known_sal
print "ppl with unkown pay", unknown_total_pay, (float(unknown_total_pay) / float(total))
print "poi with unkown pay", unknown_pay_poi, (float(unknown_pay_poi) / float(total))
