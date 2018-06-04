import feedparser
url=raw_input("enter url")
Data=feedparser.parse(r)
i=1
for post in Data.entries:
    print i,"\n",post.title+"\n"+post.published+":"+post.summary+"\n"+"#Link:"+post.link
    i=i+1
