class Song:
     def __init__(self,lyrics):
      self.lyrics=lyrics
    
     def apple(self):
      for l in self.lyrics:
       print l

doodz=Song(["jam jooom joooo","jingle bingle gloom"])
brozz=Song(["hhoooi","broooom"])  
doodz.apple()
brozz.apple()
