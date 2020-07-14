"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

spending_time = defaultdict(int)

for call in calls:
    spending_time[call[0]] += int(call[3])
    spending_time[call[1]] += int(call[3])

key = max(spending_time, key=spending_time.get)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(key, spending_time[key]))