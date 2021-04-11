import random
VacCen = []
with open ('vaccinecenters.txt') as f:
    for i in f:
        VacCen.append(i.strip())  


zip_code = "2"
zip_list = []
for i in VacCen:
    j = i.split()
    j = j[len(j) - 1]
    if j == zip_code:
        zip_list.append(i)

def zip():
    #Assigns numbers 1-50 to every vaccine center location
#Since it's zero index VacCen[0] will start with 1.
    for i in zip_list:
        zip_list[zip_list.index(i)] = str(zip_list.index(i) + 1) + ". " + i

# numdoses is a dictionary with every vaccine center and it's associated number of doses 
    num_doses = {}
    for i in zip_list:
        num_doses[i] = random.randint(900, 1900) 

# num_Moderna is a dictionary with every vaccine center and it's associated number of Moderna vaccines
    num_Moderna = {} 
    for i in zip_list:
        num_Moderna[i] = random.randint(300, 899) 

    # num_Pfizer is a dictionary with every vaccine center and it's associated number of Pfizer vaccines
    num_Pfizer = {} 
    for i in zip_list:
        num_Pfizer[i] = random.randint(300, 899)

    # num_JJ is a dictionary with every vaccine center and it's associated number of JJ vaccines
    num_JJ = {} 
    for i in zip_list:
        num_JJ[i] = random.randint(300, 899) 

    centerID = "13"
    vaccine_total = 2000
    pfizer_total = 2000
    moderna_total = 2000
    jj_total = 2000
    for i in zip_list:
        if i.split()[0] == (centerID + "."): 
            num_doses[i] = vaccine_total
            num_Moderna[i] = moderna_total
            num_Pfizer[i] = pfizer_total
            num_JJ[i] = jj_total



    def pref_M(): #if person on website prefers Moderna
        curr_val = 0 
        curr_center = 0
        for i in num_Moderna:
            if num_Moderna[i] > curr_val: 
                curr_val = num_Moderna[i]
                curr_center = zip_list.index(i) + 1 
        return(zip_list[curr_center - 1])


    def pref_P(): #if person on website prefers Pfizer
        curr_val = 0 
        curr_center = 0
        for i in num_Pfizer:
            if num_Pfizer[i] > curr_val: 
                curr_val = num_Pfizer[i]
                curr_center = zip_list.index(i) + 1 
        return(zip_list[curr_center - 1])



    def pref_JJ(): #if person on website prefers JJ
        curr_val = 0 
        curr_center = 0
        for i in num_JJ:
            if num_JJ[i] > curr_val: 
                curr_val = num_JJ[i]
                curr_center = zip_list.index(i) + 1 
        return(zip_list[curr_center - 1])


    def pref_none(): #if person on website doesn't have choice
        curr_val = 0 
        curr_center = 0
        for i in num_doses:
            if num_doses[i] > curr_val:
                curr_val = num_doses[i]
                curr_center = zip_list.index(i) + 1 
        return(zip_list[curr_center - 1]) 

    vaccine_type = input() 
    if vaccine_type == "Pfizer":
        location = pref_P()
    elif vaccine_type == "Moderna":
        location = pref_M() 
    elif vaccine_type == "Johnson & Johnson":
        location = pref_JJ() 
    elif vaccine_type == "No Preference":
        location = pref_none() 

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

    print(location_name)
    print(location_address) 

if len(zip_list) >= 1:
    zip() 
else:
#Assigns numbers 1-50 to every vaccine center location
#Since it's zero index VacCen[0] will start with 1.
    for i in VacCen:
        VacCen[VacCen.index(i)] = str(VacCen.index(i) + 1) + ". " + i

# numdoses is a dictionary with every vaccine center and it's associated number of doses 
    num_doses = {}
    for i in VacCen:
        num_doses[i] = random.randint(900, 1900) 

# num_Moderna is a dictionary with every vaccine center and it's associated number of Moderna vaccines
    num_Moderna = {} 
    for i in VacCen:
        num_Moderna[i] = random.randint(300, 899) 

    # num_Pfizer is a dictionary with every vaccine center and it's associated number of Pfizer vaccines
    num_Pfizer = {} 
    for i in VacCen:
        num_Pfizer[i] = random.randint(300, 899)

    # num_JJ is a dictionary with every vaccine center and it's associated number of JJ vaccines
    num_JJ = {} 
    for i in VacCen:
        num_JJ[i] = random.randint(300, 899) 

    centerID = "23"
    vaccine_total = 2000
    pfizer_total = 150
    jj_total = 2000
    moderna_total = 0
    for i in VacCen:
        if i.split()[0] == (centerID + "."): 
            num_doses[i] = vaccine_total
            num_Moderna[i] = moderna_total
            num_Pfizer[i] = pfizer_total
            num_JJ[i] = jj_total



    def pref_M(): #if person on website prefers Moderna
        curr_val = 0 
        curr_center = 0
        for i in num_Moderna:
            if num_Moderna[i] > curr_val: 
                curr_val = num_Moderna[i]
                curr_center = VacCen.index(i) + 1 
        return(VacCen[curr_center - 1])


    def pref_P(): #if person on website prefers Pfizer
        curr_val = 0 
        curr_center = 0
        for i in num_Pfizer:
            if num_Pfizer[i] > curr_val: 
                curr_val = num_Pfizer[i]
                curr_center = VacCen.index(i) + 1 
        return(VacCen[curr_center - 1])



    def pref_JJ(): #if person on website prefers JJ
        curr_val = 0 
        curr_center = 0
        for i in num_JJ:
            if num_JJ[i] > curr_val: 
                curr_val = num_JJ[i]
                curr_center = VacCen.index(i) + 1 
        return(VacCen[curr_center - 1])


    def pref_none(): #if person on website doesn't have choice
        curr_val = 0 
        curr_center = 0
        for i in num_doses:
            if num_doses[i] > curr_val:
                curr_val = num_doses[i]
                curr_center = VacCen.index(i) + 1 
        return(VacCen[curr_center - 1]) 

    vaccine_type = input() 
    if vaccine_type == "Pfizer":
        location = pref_P()
    elif vaccine_type == "Moderna":
        location = pref_M() 
    elif vaccine_type == "Johnson & Johnson":
        location = pref_JJ() 
    elif vaccine_type == "No Preference":
        location = pref_none() 

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

    print(location_name)
    print(location_address) 



    

