import tweepy
import json
import datetime
import N

# OAuth2.0用のキーを取得する
with open("secret.json") as f:
  secretjson = json.load(f)

# 各種キーをセット
CONSUMER_KEY = secretjson["consumer_key"]
CONSUMER_SECRET = secretjson["consumer_secret"]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = secretjson["access_token"]
ACCESS_SECRET = secretjson["access_token_secret"]
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# Twitter APIをPythonから操作するための準備完了
print('Done!')

def search(word):
  txt = word + '-http -RT -【 -/ -#'
  search_result = api.search(q=txt, count=200)
  result = search_result
  print(api.rate_limit_status()['resources']['search']['/search/tweets'])
  return result

if __name__ == "__main__":
  word = input(">>")
  
  # 書き込みモードで出力
  f = open( "twt.txt", "a" )
  
  # すべてのtextから名詞を抽出
  for r in search(word): 
    print(r.text)
    f.write(r.text)  # textの書き出し
  f.close()
