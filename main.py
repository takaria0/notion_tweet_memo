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






















"""
a = Status(
  _api = < tweepy.api.API object at 0x10c674c88 > ,
  _json = {
  'created_at': 'Tue Jul 21 08:06:52 +0000 2020',
  'id': 1285486385432936449,
  'id_str': '1285486385432936449',
  'text': 'RT @zmzizm: 手間がかかる応募書類のほうが応募者の誠実さが見えるとかいうどうしようもない発想を「コストリーシグナリング」とかいう概念で「合理的」なものだと擁護するの、合理性のスコープが局所的すぎてやばいのもあるが、端的に徳がいちじるしく低い',
  'truncated': False,
  'entities': {
    'hashtags': [],
    'symbols': [],
    'user_mentions': [{
      'screen_name': 'zmzizm',
      'name': 'matsunaga',
      'id': 67807894,
      'id_str': '67807894',
      'indices': [3, 10]
    }],
    'urls': []
  },
  'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
  'in_reply_to_status_id': None,
  'in_reply_to_status_id_str': None,
  'in_reply_to_user_id': None,
  'in_reply_to_user_id_str': None,
  'in_reply_to_screen_name': None,
  'user': {
    'id': 2374745173,
    'id_str': '2374745173',
    'name': 'たか（6歳）',
    'screen_name': 'takaria0',
    'location': '日本',
    'description': 'mechanical eng student @NagoyaUniv The Case Against Education推し https://t.co/UrM3ruF6Xr lang:zh-cn Twitter減らしてます https://t.co/IzQkzWeFyF',
    'url': 'https://t.co/DbKjAyrZPp',
    'entities': {
      'url': {
        'urls': [{
          'url': 'https://t.co/DbKjAyrZPp',
          'expanded_url': 'https://takagrow.com',
          'display_url': 'takagrow.com',
          'indices': [0, 23]
        }]
      },
      'description': {
        'urls': [{
          'url': 'https://t.co/UrM3ruF6Xr',
          'expanded_url': 'http://amzn.to/2W1rkC8',
          'display_url': 'amzn.to/2W1rkC8',
          'indices': [64, 87]
        }, {
          'url': 'https://t.co/IzQkzWeFyF',
          'expanded_url': 'http://note.com/takaria0',
          'display_url': 'note.com/takaria0',
          'indices': [113, 136]
        }]
      }
    },
    'protected': False,
    'followers_count': 475,
    'friends_count': 524,
    'listed_count': 4,
    'created_at': 'Thu Mar 06 03:28:54 +0000 2014',
    'favourites_count': 17705,
    'utc_offset': None,
    'time_zone': None,
    'geo_enabled': False,
    'verified': False,
    'statuses_count': 12529,
    'lang': None,
    'contributors_enabled': False,
    'is_translator': False,
    'is_translation_enabled': False,
    'profile_background_color': 'C0DEED',
    'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png',
    'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png',
    'profile_background_tile': False,
    'profile_image_url': 'http://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg',
    'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg',
    'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2374745173/1588764352',
    'profile_link_color': '1DA1F2',
    'profile_sidebar_border_color': 'C0DEED',
    'profile_sidebar_fill_color': 'DDEEF6',
    'profile_text_color': '333333',
    'profile_use_background_image': True,
    'has_extended_profile': True,
    'default_profile': True,
    'default_profile_image': False,
    'following': False,
    'follow_request_sent': False,
    'notifications': False,
    'translator_type': 'none'
  },
  'geo': None,
  'coordinates': None,
  'place': None,
  'contributors': None,
  'retweeted_status': {
    'created_at': 'Tue Jul 21 06:33:34 +0000 2020',
    'id': 1285462908923592704,
    'id_str': '1285462908923592704',
    'text': '手間がかかる応募書類のほうが応募者の誠実さが見えるとかいうどうしようもない発想を「コストリーシグナリング」とかいう概念で「合理的」なものだと擁護するの、合理性のスコープが局所的すぎてやばいのもあるが、端的に徳がいちじるしく低い',
    'truncated': False,
    'entities': {
      'hashtags': [],
      'symbols': [],
      'user_mentions': [],
      'urls': []
    },
    'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
    'in_reply_to_status_id': None,
    'in_reply_to_status_id_str': None,
    'in_reply_to_user_id': None,
    'in_reply_to_user_id_str': None,
    'in_reply_to_screen_name': None,
    'user': {
      'id': 67807894,
      'id_str': '67807894',
      'name': 'matsunaga',
      'screen_name': 'zmzizm',
      'location': 'tokyo',
      'description': '🦉分析美学',
      'url': 'http://t.co/k78i0dpCY0',
      'entities': {
        'url': {
          'urls': [{
            'url': 'http://t.co/k78i0dpCY0',
            'expanded_url': 'http://9bit.99ing.net',
            'display_url': '9bit.99ing.net',
            'indices': [0, 22]
          }]
        },
        'description': {
          'urls': []
        }
      },
      'protected': False,
      'followers_count': 2122,
      'friends_count': 192,
      'listed_count': 73,
      'created_at': 'Sat Aug 22 03:56:01 +0000 2009',
      'favourites_count': 9903,
      'utc_offset': None,
      'time_zone': None,
      'geo_enabled': False,
      'verified': False,
      'statuses_count': 13006,
      'lang': None,
      'contributors_enabled': False,
      'is_translator': False,
      'is_translation_enabled': False,
      'profile_background_color': 'FFFFFF',
      'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme4/bg.gif',
      'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme4/bg.gif',
      'profile_background_tile': True,
      'profile_image_url': 'http://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
      'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
      'profile_banner_url': 'https://pbs.twimg.com/profile_banners/67807894/1558464889',
      'profile_link_color': 'ABBCCF',
      'profile_sidebar_border_color': '000000',
      'profile_sidebar_fill_color': '07060F',
      'profile_text_color': '504A57',
      'profile_use_background_image': False,
      'has_extended_profile': False,
      'default_profile': False,
      'default_profile_image': False,
      'following': False,
      'follow_request_sent': False,
      'notifications': False,
      'translator_type': 'none'
    },
    'geo': None,
    'coordinates': None,
    'place': None,
    'contributors': None,
    'is_quote_status': False,
    'retweet_count': 162,
    'favorite_count': 343,
    'favorited': False,
    'retweeted': True,
    'lang': 'ja'
  },
  'is_quote_status': False,
  'retweet_count': 162,
  'favorite_count': 0,
  'favorited': False,
  'retweeted': True,
  'lang': 'ja'
},
created_at = datetime.datetime(2020, 7, 21, 8, 6, 52),
id = 1285486385432936449, id_str = '1285486385432936449',
text = 'RT @zmzizm: 手間がかかる応募書類のほうが応募者の誠実さが見えるとかいうどうしようもない発想を「コストリーシグナリング」とかいう概念で「合理的」なものだと擁護するの、合理性のスコープが局所的すぎてやばいのもあるが、端的に徳がいちじるしく低い',
truncated = False,
entities = {
  'hashtags': [],
  'symbols': [],
  'user_mentions': [{
    'screen_name': 'zmzizm',
    'name': 'matsunaga',
    'id': 67807894,
    'id_str': '67807894',
    'indices': [3, 10]
  }],
  'urls': []
},
source = 'Twitter for iPhone',
source_url = 'http://twitter.com/download/iphone',
in_reply_to_status_id = None,
in_reply_to_status_id_str = None,
in_reply_to_user_id = None,
in_reply_to_user_id_str = None,
in_reply_to_screen_name = None,
author = User(_api = < tweepy.api.API object at 0x10c674c88 > ,
_json = {
  'id': 2374745173,
  'id_str': '2374745173',
  'name': 'たか（6歳）',
  'screen_name': 'takaria0',
  'location': '日本',
  'description': 'mechanical eng student @NagoyaUniv The Case Against Education推し https://t.co/UrM3ruF6Xr lang:zh-cn Twitter減らしてます https://t.co/IzQkzWeFyF',
  'url': 'https://t.co/DbKjAyrZPp',
  'entities': {
    'url': {
      'urls': [{
        'url': 'https://t.co/DbKjAyrZPp',
        'expanded_url': 'https://takagrow.com',
        'display_url': 'takagrow.com',
        'indices': [0, 23]
      }]
    },
    'description': {
      'urls': [{
        'url': 'https://t.co/UrM3ruF6Xr',
        'expanded_url': 'http://amzn.to/2W1rkC8',
        'display_url': 'amzn.to/2W1rkC8',
        'indices': [64, 87]
      }, {
        'url': 'https://t.co/IzQkzWeFyF',
        'expanded_url': 'http://note.com/takaria0',
        'display_url': 'note.com/takaria0',
        'indices': [113, 136]
      }]
    }
  },
  'protected': False,
  'followers_count': 475,
  'friends_count': 524,
  'listed_count': 4,
  'created_at': 'Thu Mar 06 03:28:54 +0000 2014',
  'favourites_count': 17705,
  'utc_offset': None,
  'time_zone': None,
  'geo_enabled': False,
  'verified': False,
  'statuses_count': 12529,
  'lang': None,
  'contributors_enabled': False,
  'is_translator': False,
  'is_translation_enabled': False,
  'profile_background_color': 'C0DEED',
  'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png',
  'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png',
  'profile_background_tile': False,
  'profile_image_url': 'http://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg',
  'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg',
  'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2374745173/1588764352',
  'profile_link_color': '1DA1F2',
  'profile_sidebar_border_color': 'C0DEED',
  'profile_sidebar_fill_color': 'DDEEF6',
  'profile_text_color': '333333',
  'profile_use_background_image': True,
  'has_extended_profile': True,
  'default_profile': True,
  'default_profile_image': False,
  'following': False,
  'follow_request_sent': False,
  'notifications': False,
  'translator_type': 'none'
}, id = 2374745173, id_str = '2374745173', name = 'たか（6歳）', screen_name = 'takaria0', location = '日本', description = 'mechanical eng student @NagoyaUniv The Case Against Education推し https://t.co/UrM3ruF6Xr lang:zh-cn Twitter減らしてます https://t.co/IzQkzWeFyF', url = 'https://t.co/DbKjAyrZPp', entities = {
  'url': {
    'urls': [{
      'url': 'https://t.co/DbKjAyrZPp',
      'expanded_url': 'https://takagrow.com',
      'display_url': 'takagrow.com',
      'indices': [0, 23]
    }]
  },
  'description': {
    'urls': [{
      'url': 'https://t.co/UrM3ruF6Xr',
      'expanded_url': 'http://amzn.to/2W1rkC8',
      'display_url': 'amzn.to/2W1rkC8',
      'indices': [64, 87]
    }, {
      'url': 'https://t.co/IzQkzWeFyF',
      'expanded_url': 'http://note.com/takaria0',
      'display_url': 'note.com/takaria0',
      'indices': [113, 136]
    }]
  }
}, protected = False, followers_count = 475, friends_count = 524, listed_count = 4, created_at = datetime.datetime(2014, 3, 6, 3, 28, 54), favourites_count = 17705, utc_offset = None, time_zone = None, geo_enabled = False, verified = False, statuses_count = 12529, lang = None, contributors_enabled = False, is_translator = False, is_translation_enabled = False, profile_background_color = 'C0DEED', profile_background_image_url = 'http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https = 'https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile = False, profile_image_url = 'http://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg', profile_image_url_https = 'https://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg', profile_banner_url = 'https://pbs.twimg.com/profile_banners/2374745173/1588764352', profile_link_color = '1DA1F2', profile_sidebar_border_color = 'C0DEED', profile_sidebar_fill_color = 'DDEEF6', profile_text_color = '333333', profile_use_background_image = True, has_extended_profile = True, default_profile = True, default_profile_image = False, following = False, follow_request_sent = False, notifications = False, translator_type = 'none'), user = User(_api = < tweepy.api.API object at 0x10c674c88 > , _json = {
  'id': 2374745173,
  'id_str': '2374745173',
  'name': 'たか（6歳）',
  'screen_name': 'takaria0',
  'location': '日本',
  'description': 'mechanical eng student @NagoyaUniv The Case Against Education推し https://t.co/UrM3ruF6Xr lang:zh-cn Twitter減らしてます https://t.co/IzQkzWeFyF',
  'url': 'https://t.co/DbKjAyrZPp',
  'entities': {
    'url': {
      'urls': [{
        'url': 'https://t.co/DbKjAyrZPp',
        'expanded_url': 'https://takagrow.com',
        'display_url': 'takagrow.com',
        'indices': [0, 23]
      }]
    },
    'description': {
      'urls': [{
        'url': 'https://t.co/UrM3ruF6Xr',
        'expanded_url': 'http://amzn.to/2W1rkC8',
        'display_url': 'amzn.to/2W1rkC8',
        'indices': [64, 87]
      }, {
        'url': 'https://t.co/IzQkzWeFyF',
        'expanded_url': 'http://note.com/takaria0',
        'display_url': 'note.com/takaria0',
        'indices': [113, 136]
      }]
    }
  },
  'protected': False,
  'followers_count': 475,
  'friends_count': 524,
  'listed_count': 4,
  'created_at': 'Thu Mar 06 03:28:54 +0000 2014',
  'favourites_count': 17705,
  'utc_offset': None,
  'time_zone': None,
  'geo_enabled': False,
  'verified': False,
  'statuses_count': 12529,
  'lang': None,
  'contributors_enabled': False,
  'is_translator': False,
  'is_translation_enabled': False,
  'profile_background_color': 'C0DEED',
  'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png',
  'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png',
  'profile_background_tile': False,
  'profile_image_url': 'http://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg',
  'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg',
  'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2374745173/1588764352',
  'profile_link_color': '1DA1F2',
  'profile_sidebar_border_color': 'C0DEED',
  'profile_sidebar_fill_color': 'DDEEF6',
  'profile_text_color': '333333',
  'profile_use_background_image': True,
  'has_extended_profile': True,
  'default_profile': True,
  'default_profile_image': False,
  'following': False,
  'follow_request_sent': False,
  'notifications': False,
  'translator_type': 'none'
}, id = 2374745173, id_str = '2374745173', name = 'たか（6歳）', screen_name = 'takaria0', location = '日本', description = 'mechanical eng student @NagoyaUniv The Case Against Education推し https://t.co/UrM3ruF6Xr lang:zh-cn Twitter減らしてます https://t.co/IzQkzWeFyF', url = 'https://t.co/DbKjAyrZPp', entities = {
  'url': {
    'urls': [{
      'url': 'https://t.co/DbKjAyrZPp',
      'expanded_url': 'https://takagrow.com',
      'display_url': 'takagrow.com',
      'indices': [0, 23]
    }]
  },
  'description': {
    'urls': [{
      'url': 'https://t.co/UrM3ruF6Xr',
      'expanded_url': 'http://amzn.to/2W1rkC8',
      'display_url': 'amzn.to/2W1rkC8',
      'indices': [64, 87]
    }, {
      'url': 'https://t.co/IzQkzWeFyF',
      'expanded_url': 'http://note.com/takaria0',
      'display_url': 'note.com/takaria0',
      'indices': [113, 136]
    }]
  }
}, protected = False, followers_count = 475, friends_count = 524, listed_count = 4, created_at = datetime.datetime(2014, 3, 6, 3, 28, 54), favourites_count = 17705, utc_offset = None, time_zone = None, geo_enabled = False, verified = False, statuses_count = 12529, lang = None, contributors_enabled = False, is_translator = False, is_translation_enabled = False, profile_background_color = 'C0DEED', profile_background_image_url = 'http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https = 'https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile = False, profile_image_url = 'http://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg', profile_image_url_https = 'https://pbs.twimg.com/profile_images/1143497398880051201/qDwEXbI-_normal.jpg', profile_banner_url = 'https://pbs.twimg.com/profile_banners/2374745173/1588764352', profile_link_color = '1DA1F2', profile_sidebar_border_color = 'C0DEED', profile_sidebar_fill_color = 'DDEEF6', profile_text_color = '333333', profile_use_background_image = True, has_extended_profile = True, default_profile = True, default_profile_image = False, following = False, follow_request_sent = False, notifications = False, translator_type = 'none'), geo = None, coordinates = None, place = None, contributors = None, retweeted_status = Status(_api = < tweepy.api.API object at 0x10c674c88 > , _json = {
  'created_at': 'Tue Jul 21 06:33:34 +0000 2020',
  'id': 1285462908923592704,
  'id_str': '1285462908923592704',
  'text': '手間がかかる応募書類のほうが応募者の誠実さが見えるとかいうどうしようもない発想を「コストリーシグナリング」とかいう概念で「合理的」なものだと擁護するの、合理性のスコープが局所的すぎてやばいのもあるが、端的に徳がいちじるしく低い',
  'truncated': False,
  'entities': {
    'hashtags': [],
    'symbols': [],
    'user_mentions': [],
    'urls': []
  },
  'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
  'in_reply_to_status_id': None,
  'in_reply_to_status_id_str': None,
  'in_reply_to_user_id': None,
  'in_reply_to_user_id_str': None,
  'in_reply_to_screen_name': None,
  'user': {
    'id': 67807894,
    'id_str': '67807894',
    'name': 'matsunaga',
    'screen_name': 'zmzizm',
    'location': 'tokyo',
    'description': '🦉分析美学',
    'url': 'http://t.co/k78i0dpCY0',
    'entities': {
      'url': {
        'urls': [{
          'url': 'http://t.co/k78i0dpCY0',
          'expanded_url': 'http://9bit.99ing.net',
          'display_url': '9bit.99ing.net',
          'indices': [0, 22]
        }]
      },
      'description': {
        'urls': []
      }
    },
    'protected': False,
    'followers_count': 2122,
    'friends_count': 192,
    'listed_count': 73,
    'created_at': 'Sat Aug 22 03:56:01 +0000 2009',
    'favourites_count': 9903,
    'utc_offset': None,
    'time_zone': None,
    'geo_enabled': False,
    'verified': False,
    'statuses_count': 13006,
    'lang': None,
    'contributors_enabled': False,
    'is_translator': False,
    'is_translation_enabled': False,
    'profile_background_color': 'FFFFFF',
    'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme4/bg.gif',
    'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme4/bg.gif',
    'profile_background_tile': True,
    'profile_image_url': 'http://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
    'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
    'profile_banner_url': 'https://pbs.twimg.com/profile_banners/67807894/1558464889',
    'profile_link_color': 'ABBCCF',
    'profile_sidebar_border_color': '000000',
    'profile_sidebar_fill_color': '07060F',
    'profile_text_color': '504A57',
    'profile_use_background_image': False,
    'has_extended_profile': False,
    'default_profile': False,
    'default_profile_image': False,
    'following': False,
    'follow_request_sent': False,
    'notifications': False,
    'translator_type': 'none'
  },
  'geo': None,
  'coordinates': None,
  'place': None,
  'contributors': None,
  'is_quote_status': False,
  'retweet_count': 162,
  'favorite_count': 343,
  'favorited': False,
  'retweeted': True,
  'lang': 'ja'
}, created_at = datetime.datetime(2020, 7, 21, 6, 33, 34), id = 1285462908923592704, id_str = '1285462908923592704', text = '手間がかかる応募書類のほうが応募者の誠実さが見えるとかいうどうしようもない発想を「コストリーシグナリング」とかいう概念で「合理的」なものだと擁護するの、合理性のスコープが局所的すぎてやばいのもあるが、端的に徳がいちじるしく低い', truncated = False, entities = {
  'hashtags': [],
  'symbols': [],
  'user_mentions': [],
  'urls': []
}, source = 'Twitter for Android', source_url = 'http://twitter.com/download/android', in_reply_to_status_id = None, in_reply_to_status_id_str = None, in_reply_to_user_id = None, in_reply_to_user_id_str = None, in_reply_to_screen_name = None, author = User(_api = < tweepy.api.API object at 0x10c674c88 > , _json = {
  'id': 67807894,
  'id_str': '67807894',
  'name': 'matsunaga',
  'screen_name': 'zmzizm',
  'location': 'tokyo',
  'description': '🦉分析美学',
  'url': 'http://t.co/k78i0dpCY0',
  'entities': {
    'url': {
      'urls': [{
        'url': 'http://t.co/k78i0dpCY0',
        'expanded_url': 'http://9bit.99ing.net',
        'display_url': '9bit.99ing.net',
        'indices': [0, 22]
      }]
    },
    'description': {
      'urls': []
    }
  },
  'protected': False,
  'followers_count': 2122,
  'friends_count': 192,
  'listed_count': 73,
  'created_at': 'Sat Aug 22 03:56:01 +0000 2009',
  'favourites_count': 9903,
  'utc_offset': None,
  'time_zone': None,
  'geo_enabled': False,
  'verified': False,
  'statuses_count': 13006,
  'lang': None,
  'contributors_enabled': False,
  'is_translator': False,
  'is_translation_enabled': False,
  'profile_background_color': 'FFFFFF',
  'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme4/bg.gif',
  'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme4/bg.gif',
  'profile_background_tile': True,
  'profile_image_url': 'http://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
  'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
  'profile_banner_url': 'https://pbs.twimg.com/profile_banners/67807894/1558464889',
  'profile_link_color': 'ABBCCF',
  'profile_sidebar_border_color': '000000',
  'profile_sidebar_fill_color': '07060F',
  'profile_text_color': '504A57',
  'profile_use_background_image': False,
  'has_extended_profile': False,
  'default_profile': False,
  'default_profile_image': False,
  'following': False,
  'follow_request_sent': False,
  'notifications': False,
  'translator_type': 'none'
}, id = 67807894, id_str = '67807894', name = 'matsunaga', screen_name = 'zmzizm', location = 'tokyo', description = '🦉分析美学', url = 'http://t.co/k78i0dpCY0', entities = {
  'url': {
    'urls': [{
      'url': 'http://t.co/k78i0dpCY0',
      'expanded_url': 'http://9bit.99ing.net',
      'display_url': '9bit.99ing.net',
      'indices': [0, 22]
    }]
  },
  'description': {
    'urls': []
  }
}, protected = False, followers_count = 2122, friends_count = 192, listed_count = 73, created_at = datetime.datetime(2009, 8, 22, 3, 56, 1), favourites_count = 9903, utc_offset = None, time_zone = None, geo_enabled = False, verified = False, statuses_count = 13006, lang = None, contributors_enabled = False, is_translator = False, is_translation_enabled = False, profile_background_color = 'FFFFFF', profile_background_image_url = 'http://abs.twimg.com/images/themes/theme4/bg.gif', profile_background_image_url_https = 'https://abs.twimg.com/images/themes/theme4/bg.gif', profile_background_tile = True, profile_image_url = 'http://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png', profile_image_url_https = 'https://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png', profile_banner_url = 'https://pbs.twimg.com/profile_banners/67807894/1558464889', profile_link_color = 'ABBCCF', profile_sidebar_border_color = '000000', profile_sidebar_fill_color = '07060F', profile_text_color = '504A57', profile_use_background_image = False, has_extended_profile = False, default_profile = False, default_profile_image = False, following = False, follow_request_sent = False, notifications = False, translator_type = 'none'), user = User(_api = < tweepy.api.API object at 0x10c674c88 > , _json = {
  'id': 67807894,
  'id_str': '67807894',
  'name': 'matsunaga',
  'screen_name': 'zmzizm',
  'location': 'tokyo',
  'description': '🦉分析美学',
  'url': 'http://t.co/k78i0dpCY0',
  'entities': {
    'url': {
      'urls': [{
        'url': 'http://t.co/k78i0dpCY0',
        'expanded_url': 'http://9bit.99ing.net',
        'display_url': '9bit.99ing.net',
        'indices': [0, 22]
      }]
    },
    'description': {
      'urls': []
    }
  },
  'protected': False,
  'followers_count': 2122,
  'friends_count': 192,
  'listed_count': 73,
  'created_at': 'Sat Aug 22 03:56:01 +0000 2009',
  'favourites_count': 9903,
  'utc_offset': None,
  'time_zone': None,
  'geo_enabled': False,
  'verified': False,
  'statuses_count': 13006,
  'lang': None,
  'contributors_enabled': False,
  'is_translator': False,
  'is_translation_enabled': False,
  'profile_background_color': 'FFFFFF',
  'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme4/bg.gif',
  'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme4/bg.gif',
  'profile_background_tile': True,
  'profile_image_url': 'http://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
  'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png',
  'profile_banner_url': 'https://pbs.twimg.com/profile_banners/67807894/1558464889',
  'profile_link_color': 'ABBCCF',
  'profile_sidebar_border_color': '000000',
  'profile_sidebar_fill_color': '07060F',
  'profile_text_color': '504A57',
  'profile_use_background_image': False,
  'has_extended_profile': False,
  'default_profile': False,
  'default_profile_image': False,
  'following': False,
  'follow_request_sent': False,
  'notifications': False,
  'translator_type': 'none'
}, id = 67807894, id_str = '67807894', name = 'matsunaga', screen_name = 'zmzizm', location = 'tokyo', description = '🦉分析美学', url = 'http://t.co/k78i0dpCY0', entities = {
  'url': {
    'urls': [{
      'url': 'http://t.co/k78i0dpCY0',
      'expanded_url': 'http://9bit.99ing.net',
      'display_url': '9bit.99ing.net',
      'indices': [0, 22]
    }]
  },
  'description': {
    'urls': []
  }
}, protected = False, followers_count = 2122, friends_count = 192, listed_count = 73, created_at = datetime.datetime(2009, 8, 22, 3, 56, 1), favourites_count = 9903, utc_offset = None, time_zone = None, geo_enabled = False, verified = False, statuses_count = 13006, lang = None, contributors_enabled = False, is_translator = False, is_translation_enabled = False, profile_background_color = 'FFFFFF', profile_background_image_url = 'http://abs.twimg.com/images/themes/theme4/bg.gif', profile_background_image_url_https = 'https://abs.twimg.com/images/themes/theme4/bg.gif', profile_background_tile = True, profile_image_url = 'http://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png', profile_image_url_https = 'https://pbs.twimg.com/profile_images/1130914202653057024/dP25URdp_normal.png', profile_banner_url = 'https://pbs.twimg.com/profile_banners/67807894/1558464889', profile_link_color = 'ABBCCF', profile_sidebar_border_color = '000000', profile_sidebar_fill_color = '07060F', profile_text_color = '504A57', profile_use_background_image = False, has_extended_profile = False, default_profile = False, default_profile_image = False, following = False, follow_request_sent = False, notifications = False, translator_type = 'none'), geo = None, coordinates = None, place = None, contributors = None, is_quote_status = False, retweet_count = 162, favorite_count = 343, favorited = False, retweeted = True, lang = 'ja'), is_quote_status = False, retweet_count = 162, favorite_count = 0, favorited = False, retweeted = True, lang = 'ja')

"""