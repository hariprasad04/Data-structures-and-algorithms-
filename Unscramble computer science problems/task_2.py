import csv

"""
TASK 2:
The official explanation is incredibly poorly-worded. This is what I've been able to glean from some forum discussions.

Find the number that spent the most amount of time on a call (calling and receiving combined) in a single month.

Output the number, the month, and the total time (in seconds) that the number spent on a call in that month:
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
"""

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    totals = {}

    for call in list(reader):
        calling, receiving, timestamp, seconds = call
        seconds = int(seconds)

        totals[calling] = totals[calling] + seconds if calling in totals else seconds
        totals[receiving] = totals[receiving] + seconds if receiving in totals else seconds

# Retrieve the key (telephone number) of the largest value (duration)
phone_number = max(totals.keys(), key=(lambda k: totals[k]))

print(f'{phone_number} spent the longest time, {totals[phone_number]} seconds, on the phone during September 2016.')
