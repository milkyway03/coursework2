import json


def get_posts():
    with open("data/data.json", "r", encoding="utf-8") as fp:
        posts = json.load(fp)
    return posts


def get_comments():
    with open("data/comments.json", "r", encoding="utf-8") as fp:
        comments = json.load(fp)
    return comments


def get_posts_with_comments_count():

    posts = get_posts()
    comments = get_comments()

    for index, post in enumerate(posts):

        comments_count = 0

        for comment in comments:
            if comment["post_id"] == post["pk"]:
                comments_count += 1

        posts[index]["comments_count"] = comments_count

    return posts


def get_post_by_pk(post_pk):
    with open("data/data.json", "r", encoding="utf-8") as fp:
        posts = json.load(fp)
    for post in posts:
        if post['pk'] == post_pk:
            return post
    return None


def get_post_comments_by_pk(post_pk):
    with open("data/comments.json", "r", encoding="utf-8") as fp:
        comments = json.load(fp)
    post_comments = []
    for comment in comments:
        if comment['post_id'] == post_pk:
            post_comments.append(comment)
    return post_comments


def get_posts_by_word(word):
    posts = get_posts_with_comments_count()
    posts_by_word = [post for post in posts if word.lower() in post.get("content").lower()]
    return posts_by_word
