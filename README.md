# blepbot
This is a Mastodon bot that posts daily blep images to a Mastodon account.
To use this bot:

1. Place blep images in a directory named img/
2. Place post text to accompany each image in directory txt/ .
   The post text filename format must be: imagefilename.txt . 
   Example: image file img/mypic.jpg will be posted with text from txt/mypic.jpg.txt
4. Place authentication token in file 'token.secret'
5. Edit blepbot.py with server name if not using botsin.space
6. Edit run_bot.bash to set up your python environment correctly
7. Schedule run_bot.bash to run twice a day (no arguments)

For a walkthrough, see this blog post: https://rdbms-insight.com/wp/2023/creating-a-mastodon-bot-in-python/

To get a Mastodon account and/or to get authentication tokens for the account, see this blog post:
https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/
