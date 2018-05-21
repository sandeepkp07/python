import os
def walk(updates):
 for name in os.listdir(updates):
  path = os.path.join(updates, name)
  if os.path.isfile(path):
   print path
  else:
   walk(path)
walk('/home/sandeep/updates')
