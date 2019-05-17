import tweepy

import time

class Bot:
    def __init__(self):
        self.CONSUMER_KEY='ENTER CONSUMER KEY'
        self.CONSUMER_KEY_SECRET='ENTER CONSUMER KEY SECRET'
        self.ACCESS_TOKEN='Python 3.6
discord.py v0.16.12
Python modules (should be included in standard library) 
datetime
secrets
random
configparser'
        self.ACCESS_TOKEN_SECRET='ENTER ACCESS TOKEN SECRET'
        self.api = self.authenticate()
        self.user_list = []
        self.tweeted_list = set([])
        self.followed_list = set([])
        self.tobetweeted_list = set([])
        self.tobetweeteduser_list = set([])

    def authenticate(self):
        """Authenticate bot to Twitter's API via Oauth."""
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY,self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN,self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
        except:
            print "The bot was unable to authenticate"
        else:
            print "The bot has been authenticated"
            return api


    def mass_follow(self,users):
        for user in users:
            try:
                self.api.create_friendship(user)
                print "you're now following id :", user
            except:
                print "Already following id : ", user

            time.sleep(10)

    def unfollow(self,users):
        for user in users:
            try:
                self.api.destroy_friendship(user)
            except:
                print "Already unfollowed: id ", user
            else:
                print "successfully unfollowed id: ", user

            time.sleep(10)

    def retweet(self,tweetids):
        for idno in tweetids:
            try:
                self.api.retweet(idno)
            except:
                print "Retweeted stuff again!!!!! id: ", idno
            else:
                print "Successfully retweeted id: ", idno
            time.sleep(10)


    def searchquery(self,query):
        results = self.api.search(q=query)
        for result in results:

            if result.id not in self.tweeted_list:
                self.tobetweeted_list.add(result.id)

            try:
                self.tobetweeteduser_list.add(result.text.split('@')[1].split(':',1)[0])

            except:
                print "hmm"

    def retweetnfollow(self,tweetids,usrids):
        self.retweet(tweetids)
        self.mass_follow(usrids)
        self.followed_list.union(self.tobetweeteduser_list)
        self.tobetweeted_list.clear()
        self.tobetweeteduser_list.clear()

    def ownfollowers(self):

        return self.api.me().friends_count

### START STUFF ####

#### INITIALIZE ####

twitterbot = Bot()
secsper2day = 2*86400

#### SEARCH after every 5 mins ####

t0 = time.time() ### start counting time


while(1):

    twitterbot.searchquery("Retweet to win")

#print twitterbot.tobetweeted_list
#print twitterbot.tobetweeteduser_list


    twitterbot.retweetnfollow(twitterbot.tobetweeted_list, twitterbot.tobetweeteduser_list) ### follow and retweet a list of ids and screen_names

    time.sleep(5*60) ########### wait for 5 mins, chill and relax

    if time.time() - t0 >= secsper2day:  #############  if the followed time is more than 2 days, unfollow the first 50
        twitterbot.unfollow(twitterbot.followed_list[:50])
        t0 = time.time()

    elif twitterbot.ownfollowers() > 1200:
        twitterbot.unfollow(twitterbot.followed_list[:50]) ################ if the followed number is more than 1200, unfollow first 50


