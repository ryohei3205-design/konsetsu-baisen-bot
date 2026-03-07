import os
import tweepy

text = """
【今節焙煎】

深煎りの一戦。

鹿島 vs 川崎
キックオフまであと少し。

#今節焙煎
#Jリーグ
"""

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_SECRET"]
)

client.create_tweet(text=text)
