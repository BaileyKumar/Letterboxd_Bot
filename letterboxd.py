import feedparser
import requests
import datetime
from dateutil.parser import parse as parsedate
from collections import defaultdict
import time

#r = requests.head('https://letterboxd.com/mlbrulz/rss/')
#url_time = r.headers['last-modified']
#(r.headers)

old_reviews = {}
url ="https://letterboxd.com/rileyiguess/rss/"
d = feedparser.parse(url)
    #d2 = feedparser.parse('https://letterboxd.com/mlbrulz/rss/', modified = r.headers['Date'])
for key in d:
    print(d[key])
#TODO take usernames from file and loop over
# f = open("usernames.txt", "r")
# usernames = f.read().replace('\n', '').split(" ")
# print(usernames)
# old_reviews = {}
# for username in usernames:
#     old_reviews[username] = []
# print(old_reviews)
# while(1):
#
#     for username in usernames:
#         url ="https://letterboxd.com/"+username+"/rss/"
#         d = feedparser.parse(url)
#         #d2 = feedparser.parse('https://letterboxd.com/mlbrulz/rss/', modified = r.headers['Date'])
#
#         print(d)
#         #matching = d2['entries'][6]
#         print("\n"+username+"\n")
#         for item in d['entries']:
#             movie_title = item['title'].split(",")[0]
#             pub_date = item['published']
#             tup = (movie_title,pub_date)
#             if not (movie_title,pub_date) in old_reviews[username]:
#                 print(movie_title)
#                 old_reviews[username].append((movie_title,pub_date))
#                 print(getattr(item, 'letterboxd_watcheddate', ''))
#             else:
#                 break
#     time.sleep(15)
