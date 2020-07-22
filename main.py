from notion.client import NotionClient
from notion.block import VideoBlock, EmbedBlock, TextBlock
import tweepy
import json
from config import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, TWITTER_COMSUMER_KEY, TWITTER_COMSUMER_SECRET, TWITTER_BEARER_TOKEN, NOTION_TOKEN, TWITTER_USERNAME
from config import NOTION_PAGE_URL


client = NotionClient(token_v2=NOTION_TOKEN)


def main():

  auth = tweepy.OAuthHandler(TWITTER_COMSUMER_KEY, TWITTER_COMSUMER_SECRET)
  auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

  api = tweepy.API(auth)

  public_tweets = api.user_timeline()
  i = 0
  for tweet in public_tweets:

    # Replace this URL with the URL of the page you want to edit
    page = client.get_block(NOTION_PAGE_URL)
    if (tweet.in_reply_to_user_id is None) and ('retweeted_status' not in tweet._json.keys()):
      print('-----------------------')
      print("{}: {}".format(i, tweet.id))
      page.children.add_new(TextBlock, title="https://twitter.com/{}/status/{}".format(TWITTER_USERNAME,tweet.id))
    i += 1
  return


if __name__ == '__main__':
  main()