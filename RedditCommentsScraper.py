# PRAW = Python Reddit API Wrapper
import praw

# Connect to Reddit  
# Specify the user agent here 
user_agent = 'Scraping constructive comments from r/selfimprovement'
r = praw.Reddit(user_agent = user_agent)

# Copy & paste the submission ID of desired thread here
# Eg. https://www.reddit.com/r/selfimprovement/comments/1pet5w
submission_id = '1pet5w'
sub = r.get_submission(submission_id = submission_id)
sub.replace_more_comments(limit = None, threshold = 0)

# Grab all the replies under a comment
def grab(comment, replies):
    replies.append({'commentID': comment.id, 'commentBody': comment.body})
    for r in comment.replies:
        grab(r, replies)
    return replies

# array1 holds the comment & its replies
# array2 writes to file 
array2 = []
for comment in sub.comments:
    array1 = []  
    array2.append(grab(comment, array1))

# Write everything to a spreadsheet. 
with open(submission_id + '.csv', 'a') as outf:
    for i in array2:
        for j in i:
            outf.write('{0},{1}'.format(j['commentID'], j['commentBody']))