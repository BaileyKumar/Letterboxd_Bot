#Discord Bot for letterboxd

import feedparser
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import urllib.request
import urllib.parse
import re
import time
import timeit
import os

bot = commands.Bot(command_prefix = '!')
client = discord.Client()
old_reviews = {}
bot.remove_command('help')

@bot.command(pass_context=True)
async def update(ctx):
    await fetch()


async def setup():
    f = open("usernames.txt", "r")
    usernames = f.read().replace('\n', '').split(", ")
    for username in usernames:
        old_reviews[username] = []
        url ="https://letterboxd.com/"+username+"/rss/"
        d = feedparser.parse(url)
        print("\n"+username+"\n")
        for item in d['entries']:
            movie_title = item['title'].split(",")[0]
            pub_date = item['published']
            tup = (movie_title,pub_date)
            if not (movie_title,pub_date) in old_reviews[username]:
                print(movie_title)
                old_reviews[username].append((movie_title,pub_date))

async def loop_fetch():
    while(1):
        channel = bot.get_channel(554656005645139968)
        await fetch()
        await asyncio.sleep(60*60)



async def fetch():
    f = open("usernames.txt", "r")
    usernames = f.read().replace('\n', '').split(", ")
    new_movies = {}
    channel = bot.get_channel(716566909218324531)
    for username in usernames:
        new_movies[username] = []
        url ="https://letterboxd.com/"+username+"/rss/"
        d = feedparser.parse(url)
        print("\n"+username+"\n")
        for item in d['entries']:
            movie_title = item['title'].split(",")[0]
            pub_date = item['published']
            tup = (movie_title,pub_date)
            if not (movie_title,pub_date) in old_reviews[username] and not "/list/" in item['link']:
                print(movie_title)
                old_reviews[username].append((movie_title,pub_date))
                print(getattr(item, 'letterboxd_watcheddate', ''))
                await createEmbed(item,username)
            else:
                break

@bot.event
async def on_ready():
    print("I am online! I am bot ")
    await setup()
    await loop_fetch()

async def createEmbed(message,username):
    spoiler = False
    if (len(message['title'].split("-")) > 1) and ("★" in  message['title'].split("-")[-1] or "½" in  message['title'].split("-")[-1]):
        score = message['title'].split("-")[-1]
    else:
        score = ""
    if not message['letterboxd_rewatch'] == "No":
        score += "↺"
    if len(message["summary"].split(">")[-2])>=11 and message["summary"].split("p>")[-2][:11] == "Watched on ":
        review = "a"
        embed=discord.Embed(title=message["letterboxd_filmtitle"]+" ("+message["letterboxd_filmyear"]+")", url="https://letterboxd.com/"+username+"/films/diary/",description="**"+getattr(message, 'letterboxd_watcheddate', '')+score+"**", color=discord.Color.blue())
    else:

        print(score.join(message["summary"].split("p>")[3:-1]))
        embed=discord.Embed(title=message["letterboxd_filmtitle"]+" ("+message["letterboxd_filmyear"]+")", url="https://letterboxd.com/"+username+"/films/diary/", color=discord.Color.blue())
        review =""
        review = review.join(message["summary"].split("p>")[3:-1])
        print(review)
        if "<em>This review may contain spoilers.</em></ <" in review:
            print("spoiler")
            spoiler = True
            review = review[46:]
        review = review.replace("<br />","\n")[:-2]
        review = review.replace("</<","\n")
        if len(review)>1550:
            review = review [:1550] +"..."
        if spoiler:
            review = "||"+review+"||"
        print(review)
        embed.add_field(name = getattr(message, 'letterboxd_watcheddate', '')+score, value = review)
    thumbnail = message["summary"].split('"')[1]
    embed.set_author(name ="Recent diary activity from "+username, url=message['link'])
    embed.set_thumbnail(url=thumbnail)
    channel = bot.get_channel(554656005645139968)
    await channel.send(embed = embed)

bot.run("")
