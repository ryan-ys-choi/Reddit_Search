import praw

# The keyword I want to search for
keyword = "category"
# The subreddit I want to search for
subreddit_name = "USCIS"

# Create a read-only Reddit intance

reddit = praw.Reddit(
    client_id = "xQSfsstOznSI4ZtjW1k-8g",
    client_secret = "Kf1C1dckZAXiVNtu2VoYo2uA9HT0OQ",
    user_agent = "Get Comments by /u/ysysysc07",
)

print(reddit.read_only)

# Obtain 10 "hot" submissions from r/'subreddit'

for submission in reddit.subreddit(subreddit_name).hot(limit=10):
    print(submission.title)

# Retrieve all comments made to r/'subreddit'

for submission in reddit.subreddit(subreddit_name).search(query="*", limit=None):
    # replace_more method is being used to load additonal comments to make sure to capture all comments
    submission.comments.replace_more(limit=None)
    # check comments that have keyword for each submission
    for comment in submission.comments.list():
        if keyword in comment.body:
            print(comment.body)