"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

incoming_call_user = set()
outgoing_call_user = set()
texting_user = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

for call in calls:
    incoming_call_user.add(call[1])
    outgoing_call_user.add(call[0])

for text in texts:
    texting_user.add(text[0])
    texting_user.add(text[1])

telemarketers = outgoing_call_user - incoming_call_user - texting_user

for telemarketer in telemarketers:
    print(telemarketer)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

