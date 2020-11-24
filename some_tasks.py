from posts.models import Post


def do_something_with_posts():
    posts = Post.objects.all()

    for post in posts:
        print(post)
