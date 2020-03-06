import praw #used to access reddit API
import textblob as TextBlob #used to define text as sentiment 
import math 

# user agent unique identifier to determine the source of 
# network requests 


reddit = praw.Reddit(client_id = '5a0STq4nA7p36g', client_secret = 'buRpiyPNnfug-8P2_6HaBJNM1Ds', user_agent = 'subsentiment' )


with open('sb.txt') as f: #open the file sb.txt as varable name f
    day_start = 1582754871 #this is the day that we start the sentiment analysis it is in epches which are the timestamps for unix
    day_end = 1582841271 # ending time in epochs
    for line in f: 
        subreddit = reddit.subreddit(line.strip())
        sub_submissions = subreddit.submissions(day_start,day_end)
        sub_sentiment = 0
        # take the sentiment as a discrete value and then add or subtract to the overall sentiment for each of the submissions 
        # we can take the average based on the number of comments in the actual subredit
        num_comments = 0
        for submission in sub_submissions:
            if not submission.stickied:
                submission.comments.replace_more(limit = 0) # we don't want to grab stickied submissions at the top that is a reddit thing its the posts that moderators highlight on the subreddit
                # grabs the show more comments
                # take that list of comments add to the sentiment values 
                for comment in submission.comments.list():
                    #grab all of the comments and put them as a list to be able to index
                    blob = TextBlob(comment.body)
                    comment_sentiment = blob.sentiment.polarity # get the polarity of the comments 
                    sub_sentiment += comment_sentiment      
                    num_comments += 1
        print('/r' + str(subreddit.display_name)) # part of the praw subreddit to acess the display name of a subreddit
        try:
            print('Ratio: ' + str(math.floor(sub_sentiment/num_comments)) + '\n')
        except:
            print("no comment sentiment" + '\n')
            ZeroDivisionError # drop this if there are no commment sentiments    