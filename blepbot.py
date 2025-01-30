from mastodon import Mastodon
import os, random, sys, logging,time,datetime, re

#dev or prod
devmode="prod"

#base directory
basedir="/home/nroshak/blepbot/"

#   Set up Mastodon
mastodon = Mastodon(
    access_token = basedir+'token.secret',
    api_base_url = 'https://botsin.space/'
)

# set up logging
loglevel=logging.DEBUG
logging.basicConfig(level=loglevel,filename=basedir+"blepbot.log", filemode="a", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Running blepbot')

# Choose file randomly from image directory
random_file=random.choice(os.listdir(basedir+"img"))

# Do post visibility differently in dev mode 
if devmode=="dev":
    # test on specific file
    random_file="testfile.png"
    post_visibility="Direct"
else:
    post_visibility="Public"

# get image and text filenames
img_file=basedir+"img/"+random_file
logging.debug('chose file '+img_file)
post_textfile=basedir+"txt/"+random_file+".txt"

# upload the media to mastodon for posting
try:
    media = mastodon.media_post(img_file, description="Blep!")
except MastodonError:
    logging.debug('Mastodon Error posting image file '+img_file+', waiting 10s to retry')
    time.sleep(10)
    media = mastodon.media_post(img_file, description="Blep!")

# read text from text files
if os.path.isfile(post_textfile):
    logging.debug ('found post text file '+post_textfile)
    file1=open(post_textfile,"r")
    post_text=file1.read()
    file1.close()
else:
    logging.error ('**** post text file '+post_textfile+' not found!')
    post_text=("Daily #blep")


# if dev mode, prepend with test
if devmode=="dev":
    post_text="TEST POST: " +post_text

# if it's Tuesday, add TongueOutTuesday hashtag
todays_date=datetime.datetime.now()
if todays_date.strftime("%w")=='2':
    post_text+=" #TongueOutTuesday"
elif todays_date.strftime("%w")=='5':
    post_text+=" #FurballFriday"
elif todays_date.strftime("%w")=='3':
    if re.search("cat",post_text,re.IGNORECASE):
        post_text+=" #WhiskersWednesday"
elif todays_date.strftime("%w")=='6':
    if re.search("cat",post_text,re.IGNORECASE):
        post_text+=" #Caturday"

# Try to post the image.
# If the media hasn't loaded yet, it will fail, so if it fails try again in 10s
try:
    #mastodon.status_post(post_text,media_ids=media)
    mastodon.status_post(post_text,media_ids=media,visibility=post_visibility)
    logging.info('Posted file '+img_file+' with text "'+post_text+'"')
except:
    logging.info('Error making post, retrying in 10 seconds');
    time.sleep(10);
    mastodon.status_post(post_text,media_ids=media,visibility=post_visibility)
    logging.info('Posted file '+img_file+' with text "'+post_text+'"')
finally:
    logging.info('Ending run of blepbot')
  
