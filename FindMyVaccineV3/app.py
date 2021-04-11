from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_cors import CORS

app = Flask(__name__)
FlaskJSON(app)
CORS(app)

import random
VacCen = []
with open ('vaccinecenters.txt') as f:
    for i in f:
        VacCen.append(i.strip())
#Assigns numbers 1-50 to every vaccine center location
#Since its zero index VacCen[0] will start with 1.
for i in VacCen:
    VacCen[VacCen.index(i)] = str(VacCen.index(i) + 1) + ". " + i

# numdoses is a dictionary with every vaccine center and its associated number of doses 
num_doses = {}
for i in VacCen:
    num_doses[i] = random.randint(900, 1900) 

# num_Moderna is a dictionary with every vaccine center and its associated number of Moderna vaccines
num_Moderna = {} 
for i in VacCen:
    num_Moderna[i] = random.randint(300, 899) 

# num_Pfizer is a dictionary with every vaccine center and its associated number of Pfizer vaccines
num_Pfizer = {} 
for i in VacCen:
    num_Pfizer[i] = random.randint(300, 899)

# num_JJ is a dictionary with every vaccine center and its associated number of JJ vaccines
num_JJ = {} 
for i in VacCen:
    num_JJ[i] = random.randint(300, 899)

def pref_M(x): #if person on website prefers Moderna
    curr_val = 0 
    curr_center = 0
    for i in x:
        if num_Moderna[i] > curr_val: 
            curr_val = num_Moderna[i]
            curr_center = x.index(i) + 1 
    return(x[curr_center - 1])


def pref_P(x): #if person on website prefers Pfizer
    curr_val = 0 
    curr_center = 0
    for i in x:
        if num_Pfizer[i] > curr_val: 
            curr_val = num_Pfizer[i]
            curr_center = x.index(i) + 1 
    return(x[curr_center - 1])



def pref_JJ(x): #if person on website prefers JJ
    curr_val = 0 
    curr_center = 0
    for i in x:
        if num_JJ[i] > curr_val: 
            curr_val = num_JJ[i]
            curr_center = x.index(i) + 1 
    return(x[curr_center - 1])


def pref_none(x): #if person on website doesn't have choice
    curr_val = 0 
    curr_center = 0
    for i in x:
        if num_doses[i] > curr_val:
            curr_val = num_doses[i]
            curr_center = x.index(i) + 1 
    return(x[curr_center - 1])

@app.route('/confirm_submission', methods=['POST', 'GET'])
def confirm_submission():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    centerID = request.args.get("centerid");
    vaccine_total = request.args.get("vaccinetotal")
    moderna_total = request.args.get("modernatotal");
    pfizer_total = request.args.get("pfizertotal");
    jj_total = request.args.get("jjtotal");
    print(vaccine_total);
    print("*********")
    for i in VacCen:
        if i.split()[0] == (centerID + "."): 
            num_doses[i] = int(vaccine_total)
            num_Moderna[i] = int(moderna_total)
            num_Pfizer[i] = int(pfizer_total)
            num_JJ[i] = int(jj_total)
    return json_response()

@app.route('/getlocation', methods=['GET'])
def get_location():
    vaccine_type = request.args.get("vaccinetype")
    zipcode = request.args.get("zipcode")
    UserList = VacCen
    print(zipcode)
    zip_list = []
    for i in VacCen:
        j = i.split()
        j = j[len(j) - 1]
        if j == zipcode:
            zip_list.append(i)
    print(zip_list)
    if len(zip_list) >= 1:
        UserList = zip_list
    print(UserList)
    if vaccine_type == "pfizer":
        location = pref_P(UserList)
    elif vaccine_type == "moderna":
        location = pref_M(UserList) 
    elif vaccine_type == "johnson":
        location = pref_JJ(UserList) 
    elif vaccine_type == "0":
        location = pref_none(UserList)
    location = location.split()[1:]
    count = 0
    for i in location:
        try:
            int(i) 
            count = location.index(i) 
            break
        except: 
            continue

    location_name = location[0:count] 
    location_address = location[count:]

    location_name = " ".join(location_name)
    location_address = " ".join(location_address)
    return json_response(name=location_name, location=location_address, type=vaccine_type);

if __name__ == '__main__':
    app.run()