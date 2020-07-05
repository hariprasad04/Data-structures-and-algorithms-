import csv

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def dedupe_list(input):
    """Remove duplicates from the given list"""
    return list(set(input))


numbers = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        numbers.extend(text[:2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        numbers.extend(call[:2])

numbers = dedupe_list(numbers)
print(f'There are {len(numbers)} different telephone numbers in the records.')


