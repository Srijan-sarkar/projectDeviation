import csv
import math

with open('C:/Users/Asus/Desktop/whj/project 105/data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

#finding mean
def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total+ int(i)
    mean = total/n
    return mean

#squaring and getting the values

squared_list=[]

for i in data:
    a = int(i) - mean(data)
    a = a**2
    squared_list.append(a)

#getting sum
sum = 0
for i in squared_list:
    sum = sum + i

#dividing the sum by the total values
result = sum/ (len(data)-1)

# getting the deviation by taking square root of the result
sd = math.sqrt(result)

print(sd)