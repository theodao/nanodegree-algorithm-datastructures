"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

unique_telephone = set()

for text in texts:
    unique_telephone.add(text[0])
    unique_telephone.add(text[1])

for call in calls:
    unique_telephone.add(call[0])
    unique_telephone.add(call[1])

print("There are {} different telephone numbers in the records".format(len(unique_telephone)))

"""`
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
