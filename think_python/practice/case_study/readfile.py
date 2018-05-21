f = open('abc.txt')
for sentence in f:
 w = sentence.strip()
 if len(w) > 20:
  print w

