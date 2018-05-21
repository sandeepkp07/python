class LinearMap:
    def __init__(self):
        self.items = []
    
    def add(self,k,v):
        self.items.append((k,v))
    
    def get(self,k):
        for key,val in self.items:
            if key == k:
                return val
        raise KeyError

class BetterMap:
    def __init__(self,n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())


    def find_map(self,k):
        index = hash(k) % len(self.maps)
        return self.maps[index]


    
    def add(self,k,v):
        m=self.find_map(k)
        m.add(k,v)

    def get(self,k):
        m=self.find_map(k)
        return m.get(k)
    

        
p=LinearMap()
p.add(2,4)
p.get((2))
f = BetterMap()
f.add(3,5)
print f.get(3)
print f.find_map(3)
