import tweepy
import time 

<<<<<<< HEAD
auth = tweepy.OAuthHandler('XX','YY') # access code unique to your account 
auth.set_access_token('ZZ','AA')
=======
auth = tweepy.OAuthHandler('XX','YY') # note: access keys and passwords should be generated and linked to your own account
auth.set_access_token('AA','BB')
>>>>>>> 6f496e51f55bacbf360d5e0fe9ffe4ecb8d899ba

api = tweepy.API(auth, wait_on_rate_limit =  True, wait_on_rate_limit_notify = True)
user = api.me()

FILE_NAME = 'post.txt'

def read_last_seen(FILE_NAME):
        file_read = open(FILE_NAME, 'r')
        last_seen_id = int(file_read.read().strip())
        file_read.close()
        return last_seen_id

def store_last_seen(FILE_NAME):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')

for tweet in tweets: 
    
    if '#ultimatebot' in tweet.full_text.lower():
        print(str(tweet.id) + ' - ' + tweet.full_text)
        api.update_status("@" + tweet.user.screen_name + " Auto reply works :)", tweet_id)
        store_last_seen(FILE_NAME, tweet.id) 

# search = 'WayV'
# numberOfTweets = 5 ## limit fo 500 
# count = 0 
# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#     try: 
#         print('Tweet Liked')
#         tweet.favorite()
#         tweet.retweet()
#         count = count + 1
#         api.update_status('WayV Tweet Liked. User:' + tweet.user.screen_name)
#         time.sleep(2)
#     except tweepy.TweepError as e: 
#         print(e.reason)
#     except StopIteration:
#         break



# for follower in tweepy.Cursor(api.followers).items():  ## to find name of followers 
#     print(follower.name)
