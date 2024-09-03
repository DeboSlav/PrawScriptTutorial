import praw


reddit = praw.Reddit (
username = "placeholder",
password = "placeholder",
client_id = "placeholder",
client_secret = "placeholder",
user_agent = "placeholder"
)


subreddit = reddit.subreddit("python")


top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)


for post in top_posts:
    print("\n")
    print("Title - ", post.title)
    print("ID - ", post.id)
    print("Author - ", post.author)
    print("URL - ", post.url)
    print("Score - ", post.score)
    print("Comment count - ", post.num_comments)
    print("Created - ", post.created_utc)
    print("\n")

post = reddit.submission(id="hqc7ol")

comments = post.comments

for comment in comments[:2]:
    print("Printing comment...")
    print("Comment body - ", comment.body)
    print("Author - ", comment.author)
    print("\n")

