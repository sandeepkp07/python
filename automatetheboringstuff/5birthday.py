birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print ('enter a name: (blank to exit)')
    name = raw_input()
    if name == '':
        break
    if name in birthdays:
        print (birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print("what is his bday?")
        bday = raw_input()
        birthdays[name] = bday
        print "updated"
        print birthdays
