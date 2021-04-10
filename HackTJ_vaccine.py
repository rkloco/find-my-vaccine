import random
VacCen = []
with open ('vaccinecenters.txt') as f:
    for i in f:
        VacCen.append(i.strip())  


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

type_Vac = input("Which vaccine provider do you prefer? ")

if type_Vac.lower() == "pfizer":
    print(pref_P())
elif type_Vac.lower() == "moderna":
    print(pref_M())
elif type_Vac.lower() == "Johnson & Johnson":
    print(pref_JJ()) 
elif type_Vac.lower() == "no preference":
    print(pref_none()) 
    

