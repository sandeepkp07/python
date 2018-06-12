import requests
import ast

def converter(cfrm,cto,amt):
    res=requests.get("https://api.fixer.io/latest?base="+cfrm)
    text = ast.literal_eval(res.text)
    print text
    rates = text["rates"]
    print "YOU CAN CONVERT IT TO:\n",rates.keys()
    amount = (rates[cto])*(float(amt))
    print str(amount)
print("Enter the currency name in capital letters(3 letters)")
cfrm = raw_input("convert from:")
cto =raw_input("convert to")
amt = input("amount:")
converter(cfrm,cto,amt)
