import os
def walk(dir):
 try:
  names=[]
  for name in os.listdir(dir):
   path=os.path.join(dir,name)
   if os.path.isfile(path):
    names.append(path)
   else:
    names.extend(walk(path))
  return names
 except:
  print "nop"

def checksum(x):
 cmd = 'md5sum ' + x
 return pipe(cmd)

def pipe(cmd):
 fp = os.popen(cmd)
 res = fp.read()
 print res
 stat = fp.close()
 stat = None
 return res, stat


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def checkpairs(names):
  for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
  return True

def compute_checksums(dirname,suffix):
 names = walk(dirname)
 d={}
 for name in names:
  if name.endswith(suffix):
   res,stat = checksum(name)
   ch,_ = res.split()
   if ch in d:
    d[ch].append(name)
   else:
    d[ch] = [name]
 return d

def duplicates(d):
 for key, names in d.iteritems():
        if len(names) > 1:
            print 'The following files have the same checksum:'
            for name in names:
                print name

            if checkpairs(names):
                print 'And all other songs are identical.'


if __name__ == '__main__':
    d = compute_checksums(dirname='ss', suffix='.mp3')
    print duplicates(d)

