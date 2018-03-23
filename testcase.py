import json
from random import randint,sample,uniform

def parse_json(address):
    with open(address) as data_file:    
        data = json.load(data_file)
    return data

# address = str(input('Enter Address: '))
address = 'interlink.json'
schema = parse_json(address)
properties = schema['properties']
no_of_properties = len(properties)

dataset_titles = []

for i in list(properties.keys()):
    dataset_titles.append(i)

upper=7
lower=3
length = len(dataset_titles)*upper
l = 100 #no. of mines to be generated
f = open('testoutput.csv', 'w')
f.write("sl. no.")

for i in range(length):
    f.write(","+dataset_titles[i%2])
    
for i in range(l):
    f.write('\n')
    f.write(str(i+1));
    n = randint(lower, upper); #no. of hydraulic fluids used by a mine
    hNos = sample(range(1, 50, 1), n)
    sum = 0.0
    usageH = []
    
    for j in range(n):
        usageH.append(uniform(1.0, 100.0))
        sum += usageH[j]
        
    for j in range(n):
        usageH[j] = (usageH[j]*100)/sum
        f.write(",")
        f.write(str(hNos[j]))
        f.write(",")
        f.write(str(usageH[j]))
        
    for j in range(length-n*2):
        f.write(",")
        f.write(str(None))
        
f.close()