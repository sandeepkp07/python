def trimtree(tree):
    p = tree[1]
    if type(p) == type(""):
        return p
    else:
        return (trimtree(p[0]),trimtree(p[1]))



def buildtree(tuples):
    while len(tuples) > 1:
        leasttwo=tuple(tuples[0:2])
        therest=tuples[2:]
        combfreq=leasttwo[0][0] + leasttwo[1][0]
        tuples = therest + [(combfreq,leasttwo)]
        tuples.sort()
    return trimtree(tuples[0])






def sortfreq(freq):
    letters = freq.keys()
    tuples = []
    for let in letters:
        tuples.append((freq[let],let))
    tuples.sort()
    return buildtree(tuples)




def frequency(str):
    freq={}
    for ch in str:
        freq[ch]=freq.get(ch,0) + 1
    print sortfreq(freq)
 
a="Iam the happiest"
print frequency(a)
