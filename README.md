# Giveawaybot

Okay, so this is a twitter giveawaybot coded in python with tweepy.

It searches for contests on twitter for which you have to follow and retweet their tweets.

You'll have to enter your CONSUMER KEY, ACCESS TOKEN and other Twitter app details in main.py

The algorithm is simple:

1. Connect to twitter
2. Search for tweets with "Retweet to win" query
3. Retweet and follow the tweets and users respectively
4. Wait for some time (5 mins)
5. If it has been over 2 days after following certain accounts, unfollow the first 50
6. If the number of followed accounts is greater than 1200, unfollow first 50

Step 6. is because, twitter sets the number of people you could follow based upon the number of people following you.
Also, it was a fun project, so there's was no necessary need to follow more than 1200 people :D

Using the Original source author for a particular tweet was hard with tweepy, so the code extracts the tweet text, splits it so that it's highly probable that one gets the Original Author's screen_name

This has been implemented with the split statements on line 73 in main.py

Feel free to contribute. Feel free to use.

Apologies for a NOT SO NEAT code, but I'm a simulation engineer and don't care for neatness :D

