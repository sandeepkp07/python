import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
print vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
                            
