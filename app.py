from flask import Flask, request, render_template
from functions import get_posts_with_comments_count, get_post_by_pk, get_post_comments_by_pk
app = Flask(__name__)


@app.route('/',)
def page_index():
    posts = get_posts_with_comments_count()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_pk>',)
def page_post(post_pk):

    post = get_post_by_pk(post_pk)
    comments = get_post_comments_by_pk(post_pk)
    comments_count = len(comments)

    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)


@app.route('/search',)
def page_search():
    key_word = request.args.get("s")
    if key_word:
        s = key_word.lower()
        posts = get_posts_with_comments_count()
        found_posts = [post for post in posts if s in post.get("content").lower()]
    else:
        return get_posts_with_comments_count()

    found_posts = found_posts[:10]
    return render_template("search.html", found_posts=found_posts)


app.run()
