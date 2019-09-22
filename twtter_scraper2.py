from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import ssl

print('scrape to file - twitter\n')
url = 'https://twitter.com/PresidentIRL'

ctx = ssl._create_unverified_context()
html = urlopen(url, context=ctx)
soup = BS(html, 'html.parser')

alltweets = []
timeline = soup.select('#timeline li.stream-item')

# going into each tweet/ li node
for tweet in timeline:
    # 'data-item-id' is an attribute of the li tag - no navigation needed
    tweet_id = tweet['data-item-id']
    # p tag of class text-tweet nested in li
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    alltweets.append({"id": tweet_id, "text": tweet_text})

for tweet in alltweets:
    print(tweet)

fname = 'harvest.txt'
fhandle = open('harvest.txt', 'w')

for tweet in alltweets:
    fhandle.write(tweet['id'])
    fhandle.write('\n')
    fhandle.write(tweet['text'])
    fhandle.write('\n'*3)

print('\nHarvested.')