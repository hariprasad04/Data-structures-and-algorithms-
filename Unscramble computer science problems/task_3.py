import csv
import re

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

landline_pattern = re.compile(r'^\((0[0-9]+)\)')


def dedupe_list(input):
    """Remove duplicates from the given list"""
    return list(set(input))


def is_bangalore_number(phone_number):
    """Determine whether the given telephone number is from Bangalore"""
    return phone_number[:5] == '(080)'


def is_telemarketer(phone_number):
    """Determine whether the given telephone number is a know telemarketer"""
    return phone_number[:3] == '140'


def is_mobile(phone_number):
    """Determine whether the given telephone number belongs to a mobile (cell) phone"""
    return phone_number[:1] in ['7', '8', '9']


def is_landline(phone_number):
    """Determine whether the given telephone number belongs to a landline (fixed line)"""
    return landline_pattern.match(phone_number) is not None


def extract_area_code(phone_number):
    """
    Extract the area code from the given number

    If a valid area code is not found, return an empty string
    """
    if is_telemarketer(phone_number):
        return '140'
    if is_mobile(phone_number):
        return phone_number[:4]
    if is_landline(phone_number):
        return landline_pattern.match(phone_number).group(1)
    return ''


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    total_from_bangalore = 0
    total_to_bangalore = 0
    area_codes = []

    for call in calls:
        calling, receiving, timestamp, seconds = call

        # We only care about calls originating in Bangalore
        if not is_bangalore_number(calling):
            continue

        # Ignore calls where we can't determine the recipient's area code
        area_code = extract_area_code(receiving)
        if not area_code:
            continue

        area_codes.append(area_code)
        total_from_bangalore += 1

        if is_bangalore_number(receiving):
            total_to_bangalore += 1

# Remove duplicates and sort
area_codes = sorted(dedupe_list(area_codes))

# Part A:
print('The numbers called by people in Bangalore have codes:')
for area_code in area_codes:
    print(area_code)

# Part B:
bang_bang = '{:,.2%}'.format(total_to_bangalore / total_from_bangalore)
print(f'{bang_bang} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
