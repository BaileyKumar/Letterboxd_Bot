# pretty ={'title': 'The Matrix, 1999 - ★★★★★', 'title_detail': {'type': 'text/plain', 'language': 'en-US', 'base': 'https://letterboxd.com/rileyiguess/rss/', 'value': 'The Matrix, 1999 - ★★★★★'}, 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://letterboxd.com/rileyiguess/film/the-matrix/'}], 'link': 'https://letterboxd.com/rileyiguess/film/the-matrix/', 'id': 'letterboxd-review-143640262', 'guidislink': False, 'published': 'Wed, 6 Jan 2021 10:53:15 +1300', 'published_parsed': "time.struct_time(tm_year=2021, tm_mon=1, tm_mday=5, tm_hour=21, tm_min=53, tm_sec=15, tm_wday=1, tm_yday=5, tm_isdst=0)", 'letterboxd_watcheddate': '2021-01-05', 'letterboxd_rewatch': 'No', 'letterboxd_filmtitle': 'The Matrix', 'letterboxd_filmyear': '1999', 'letterboxd_memberrating': '5.0', 'summary': '<p><img src="https://a.ltrbxd.com/resized/film-poster/5/1/5/1/8/51518-the-matrix-0-500-0-750-crop.jpg?k=a16e521eb2" /></p> <p>lol this movie is so sick cant believe it took me this long to watch it</p>', 'summary_detail': {'type': 'text/html', 'language': 'en-US', 'base': 'https://letterboxd.com/rileyiguess/rss/', 'value': '<p><img src="https://a.ltrbxd.com/resized/film-poster/5/1/5/1/8/51518-the-matrix-0-500-0-750-crop.jpg?k=a16e521eb2" /></p> <p>lol this movie is so sick cant believe it took me this long to watch it</p>'}, 'authors': [{'name': 'riley'}], 'author': 'riley', 'author_detail': {'name': 'riley'}}
# # {'title': 'The Killing of a Sacred Deer, 2017 - ★★', 'title_detail': {'type': 'text/plain', 'language': 'en-US', 'base': 'https://letterboxd.com/mlbrulz/rss/', 'value': 'The Killing of a Sacred Deer, 2017 - ★★'}, 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://letterboxd.com/mlbrulz/film/the-killing-of-a-sacred-deer/'}], 'link': 'https://letterboxd.com/mlbrulz/film/the-killing-of-a-sacred-deer/', 'id': 'letterboxd-watch-143533214', 'guidislink': False, 'published': 'Tue, 5 Jan 2021 21:01:41 +1300', 'published_parsed': "time.struct_time(tm_year=2021, tm_mon=1, tm_mday=5, tm_hour=8, tm_min=1, tm_sec=41, tm_wday=1, tm_yday=5, tm_isdst=0)", 'letterboxd_watcheddate': '2021-01-05', 'letterboxd_rewatch': 'No', 'letterboxd_filmtitle': 'The Killing of a Sacred Deer', 'letterboxd_filmyear': '2017', 'letterboxd_memberrating': '2.0', 'summary': '<p><img src="https://a.ltrbxd.com/resized/film-poster/3/3/3/3/1/0/333310-the-killing-of-a-sacred-deer-0-500-0-750-crop.jpg?k=ac106ab286" /></p> <p>Watched on Tuesday January 5, 2021.</p>', 'summary_detail': {'type': 'text/html', 'language': 'en-US', 'base': 'https://letterboxd.com/mlbrulz/rss/', 'value': '<p><img src="https://a.ltrbxd.com/resized/film-poster/3/3/3/3/1/0/333310-the-killing-of-a-sacred-deer-0-500-0-750-crop.jpg?k=ac106ab286" /></p> <p>Watched on Tuesday January 5, 2021.</p>'}, 'authors': [{'name': 'mlbrulz'}], 'author': 'mlbrulz', 'author_detail': {'name': 'mlbrulz'}}
#
#
# for key in pretty:
#     print(key)
#     if isinstance(pretty[key], dict):
#         for key2 in pretty[key]:
#             print(pretty[key][key2])
#         print("\n\n")
#     else:
#         print(pretty[key])
#         print("\n\n")
review = "<em>This review may contain spoilers.</em></ <asdf</<dfa<br />d</<D</"
spoiler = False
if "<em>This review may contain spoilers.</em></ <" in review:
    print("spoiler")
    spoiler = True
    review = review[46:]
review = review.replace("<br />","\n")[:-2]
review = review.replace("</<","\n")
if len(review)>1750:
    review = review [:1750] +"..."
if spoiler:
    reivew = "||"+review+"||"
print(review)
