
import praw
import time

ignoreSubs = {}
daysToKeep = 0

timeToKeep = daysToKeep * 60 * 60 * 24

def login():
    f = open("RedEraser-Token", "r")
    my_client_id = f.readline().strip('\n') 
    my_client_secret = f.readline().strip('\n')
    my_refresh_token = f.readline().strip('\n')
    f.close()
    r = praw.Reddit(user_agent="Red Eraser / v 2.0", 
            client_id=my_client_id,
            client_secret=my_client_secret,
            refresh_token=my_refresh_token)
    print(r.user.me())
    return r.user.me()

def deleteComments(user):

    cscore_min = 200
    cscore_tot = 0
    currenttime = time.time()
    print("Deleting comments now")

    commentsDeleted = 0

    cgen = user.comments.new(limit=None)

    for c in cgen:

        if str(c.subreddit).lower() in ignoreSubs:
            print("Ignoring")
            continue

        if (currenttime - c.created_utc > timeToKeep):
            c.edit('#')
            c.delete()
            commentsDeleted += 1
            print("Comment deleted")

        if commentsDeleted % 10 == 0:
            print("{0} comments deleted".format(commentsDeleted))

    if commentsDeleted != 0:
        print("Total of {0} comments deleted".format(commentsDeleted))

    return commentsDeleted

def deletePosts(user):

    currenttime = time.time()
    print("Deleting posts now")
    postsDeleted = 0
    postsFound = 0

    for o in range(0,999999999):

        postFound = 0

        for p in user.submissions.new(limit=100):

            postsFound += 1

            if str(p.subreddit).lower() in ignoreSubs:
                print("Ignoring")
                continue

            if (currenttime - p.created_utc > timeToKeep):
                if p.selftext:
                    p.edit('#')
                p.delete()
                postsDeleted += 1

            if postsDeleted % 10 == 0:
                print("{0} posts deleted".format(postsDeleted))

        if postsFound < 100:
            print("Done.")
            break

    if postsDeleted != 0:
        print("Total of {0} posts deleted".format(postsDeleted))

    return postsDeleted

def main():
    try:
        user = login()
    except Exception as e:
        print("Login failed due to: ")
        print(str(e))
        return

    try:
        commentsDeleted = deleteComments(user)
    except Exception as e:
        print("Comment deletion failed due to: ")
        print(str(e))
        return

    try:
        postsDeleted = deletePosts(user)
    except Exception as e:
        print("Post deletion failed due to: ")
        print(str(e))
        return

    print("Total of {0} comments and {1} posts deleted".format(commentsDeleted,
        postsDeleted))

if __name__ == "__main__":
    main()
