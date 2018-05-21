import sys
def anagram(x):
 d = {}
 for line in x:
  r = line.strip().lower()
  t = list(r)
  t.sort()
  t = ''.join(t)
  if t not in d:
   d[t] = [r]
  else:
   d[t].append(r)
 t=[]
 for v in d.values():
  if len(v) > 1:
   t.append((len(v), v))
<<<<<<< HEAD
   t.sort(reverse=True)
=======
   t.sort(reverse=true)
>>>>>>> 942fcdc9ac69882613baf0ec070455e816d890a9
 for y,z in t:
  print z
a=open('anagram.txt')
print anagram(a)
