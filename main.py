"""
Create config.py and set appropriate variables in the file before running.
"""
import json
from datetime import date

from notion.client import NotionClient
from notion.block import VideoBlock, EmbedBlock, TextBlock, HeaderBlock
import tweepy

from config import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, TWITTER_COMSUMER_KEY, TWITTER_COMSUMER_SECRET, TWITTER_BEARER_TOKEN, NOTION_TOKEN, TWITTER_USERNAME
from config import NOTION_PAGE_URL

client = NotionClient(token_v2=NOTION_TOKEN)

def main():
  """ 
  You need to get these keys and secrets from twitter API 
  https://developer.twitter.com/en
  """
  auth = tweepy.OAuthHandler(TWITTER_COMSUMER_KEY, TWITTER_COMSUMER_SECRET)
  auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
  api = tweepy.API(auth)
  public_tweets = api.user_timeline()

  """
  Set the notion page that you want to edit
  """
  page = client.get_block(NOTION_PAGE_URL)
  page.children.add_new(HeaderBlock, title="{}".format(date.today()))

  i = 0
  """ print raw URL of tweets to the page """
  for tweet in public_tweets:
    if (tweet.in_reply_to_user_id is None) and ('retweeted_status' not in tweet._json.keys()):
      print('-----------------------')
      print("{}: {}".format(i, tweet.id))
      page.children.add_new(TextBlock, title="{}:\nhttps://twitter.com/{}/status/{}".format(i, TWITTER_USERNAME,tweet.id))
      i += 1

  i = 0
  """ print embedded tweets to the page """
  for tweet in public_tweets:
    if (tweet.in_reply_to_user_id is None) and ('retweeted_status' not in tweet._json.keys()):
      page.children.add_new(TextBlock, title="{}:".format(i))
      page.children.add_new(EmbedBlock, source="https://twitter.com/{}/status/{}".format(TWITTER_USERNAME,tweet.id))
    i += 1

  return


if __name__ == '__main__':
  main()