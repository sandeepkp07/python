import shelve
s = shelve.open("text.txt")
c = ["sd","ac","sca"]
s["c"] = c
s.close()
print s
