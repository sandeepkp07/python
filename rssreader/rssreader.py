import feedparser
url=raw_input("enter url")
Data=feedparser.parse(r)
i=1
<<<<<<< HEAD
v=[]
DATA=[]
for post in f.entries:
    DATA.append(post.title+"\n"+post.published+":"+post.summary+"\n"+"#Link:"+post.link)
    for i in DATA:
        print i
=======
for post in Data.entries:
    print i,"\n",post.title+"\n"+post.published+":"+post.summary+"\n"+"#Link:"+post.link
    i=i+1
>>>>>>> a53eac48d56c4f16c359c3322d77bffb9d116deb
