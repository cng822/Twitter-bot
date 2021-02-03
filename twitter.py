import tweepy
import time 

auth = tweepy.OAuthHandler('XX','YY') # note: access keys and passwords should be generated and linked to your own account
auth.set_access_token('AA','BB')

api = tweepy.API(auth, wait_on_rate_limit =  True, wait_on_rate_limit_notify = True)
user = api.me()

search = 'WayV'
numberOfTweets = 5 ## limit fo 500 

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try: 
        print('Tweet Liked')
        tweet.favorite()
        tweet.retweet()
        api.update_status('WayV Liked')
        time.sleep(20)
        # tweet.destroy_favorite()
    except tweepy.TweepError as e: 
        print(e.reason)
    except StopIteration:
        break


# for follower in tweepy.Cursor(api.followers).items():  ## to find name of followers 
#     print(follower.name)
