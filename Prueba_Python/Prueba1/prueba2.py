import tweepy

consumer_key = "Vf19idOabT6ynBvhFaR64V6lv" #Your API/Consumer key 
consumer_secret = "X5hAsdejDMtWlQqyS0wX9hf0BrAYP3OjUlDfOJNEQttLe6l1uf" #Your API/Consumer Secret Key
access_token = "2297674277-osqRIQUgYRChKwYomkBsIHhd2AVg2fQXU9Gkgqn"    #Your Access token key
access_token_secret = "fqusTteweBHJqqLxtS3htDHYnh51BmZyJlGgajroJLLzr" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


username = "migueclon98"
no_of_tweets =100


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    
except BaseException as e:
    print('Status Failed On,',str(e))
    