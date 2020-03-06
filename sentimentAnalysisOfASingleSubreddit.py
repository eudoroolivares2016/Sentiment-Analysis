import praw #used to access reddit API
import textblob
from textblob import TextBlob #used to define text as sentiment 
import math

# user agent unique identifier to determine the source of 
# network requests 

#TODO make the day start and end environment variable or write a subscript that turns normal days into epoch times

reddit = praw.Reddit(client_id = '5a0STq4nA7p36g', client_secret = 'buRpiyPNnfug-8P2_6HaBJNM1Ds', user_agent = 'subsentiment' )
day_start = 1582754871 #this is the day that we start the sentiment analysis it is in epches which are the timestamps for unix
day_end = 1582841271 # ending time in epochs
subreddit = reddit.subreddit('memes')
print(subreddit.subscribers)
sub_sentiment = 0
num_comments = 0

Limit = 25
file1 = open("hi.txt", 'w+')
for comment in subreddit.comments(limit= 4): # TODO make limit be defined by an environment variable
    #print(comment.author)

    blob = TextBlob(comment.body)
    try:
        file1.write(comment.body + '\n')
    except:
        file1.write("Bad Line" + '\n')
    
    comment_sentiment = blob.sentiment.polarity # get the polarity of the comments 
    sub_sentiment += comment_sentiment      
    num_comments += 1
    sentimentPercent = (math.ceil(sub_sentiment/num_comments))    
#print( "Sentiment percent for the last " + str(Limit) + " on the subreddit " + subreddit.display_name + " " + str(sentimentPercent) + " %")

goodString = "this is not the best thing"
blob2 = TextBlob(goodString)
print(blob2.sentiment.polarity)

#sub_submissions = subreddit.submissions(day_start,day_end)
#subreddit.
# sub_sentiment = 0
# num_comments = 0
# for submission in sub_submissions:
#     if not submission.stickied:
#         submission.comments.replace_more(limit = 0) # we don't want to grab stickied submissions at the top that is a reddit thing its the posts that moderators highlight on the subreddit
#         for comment in submission.comments.list():
#             blob = TextBlob(comment.body)
#             comment_sentiment = blob.sentiment.polarity # get the polarity of the comments 
#             sub_sentiment += comment_sentiment      
#             num_comments += 1
# print(subreddit.display_name)
# try:
#     print('Ratio: ' + str(math.floor(sub_sentiment/num_comments)) + '\n')
# except:
#     print("no comment sentiment" + '\n')
#     ZeroDivisionError # drop this if there are no commment sentiments    
