import feedparser
r=raw_input("enter url")
f=feedparser.parse(r)
i=1
v=[]
DATA=[]
for post in f.entries:
    DATA.append(post.title+"\n"+post.published+":"+post.summary+"\n"+"#Link:"+post.link)
    for i in DATA:
        print i
