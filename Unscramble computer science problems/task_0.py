import csv

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    sending, receiving, timestamp = list(reader)[0]
    print(f'First record of texts, {sending} texts {receiving} at time {timestamp}')

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calling, receiving, timestamp, seconds = list(reader)[-1]
    print(f'Last record of calls, {calling} calls {receiving} at time {timestamp}, lasting {seconds} seconds')

