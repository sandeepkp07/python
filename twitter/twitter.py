import pprint
import json
from requests_oauthlib import OAuth1Session
API_KEY = "9MrHmZOusg7wAw5JwGAg8Jy3C"
API_SECRET = "lBV7mhD6dyh5pw2NNpKh1adufBzZav8fbu04D1qMfelXTFjZxa"
AUTH = OAuth1Session(API_KEY,API_SECRET)


def tweets(username):
    user_timeline= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=2""&tweet_mode=extended"
    USER=AUTH.get(user_timeline)
    if(USER.status_code == 404):
     print "Please check username!!!!"
    else:    
     print "TWEETS:\n" 
     TWEETS = json.loads(USER.text)
     DATA=[]
     for i in TWEETS:
        print(i["full_text"]) 
     


USER_NAME = raw_input("enter your Twitter UserName:")
tweets(USER_NAME)
