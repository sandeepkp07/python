import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
m = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + m.group())
