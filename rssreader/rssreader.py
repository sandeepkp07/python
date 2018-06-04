import feedparser
r=raw_input("enter url")
f=feedparser.parse(r)
i=1
for post in f.entries:
    print i,"\n",post.title+"\n"+post.published+":"+post.summary+"\n"+"#Link:"+post.link
    i=i+1
