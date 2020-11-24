from django.core.management.base import BaseCommand, CommandError
from posts.models import Post


class Command(BaseCommand):
    help = 'My Custom Command'

    def add_arguments(self, parser):
        parser.add_argument('post_ids', nargs='*', type=int)

    def handle(self, *args, **options):
        posts = []

        if options['post_ids']:
            posts = Post.objects.filter(id__in=options['post_ids'])
        else:
            posts = Post.objects.all()

        if not posts:
            return self.stdout.write(self.style.ERROR('No Posts'))

        for post in posts:
            self.stdout.write(f'ID: {post.id} BODY: {post.body}')

        self.stdout.write(self.style.SUCCESS('Success!'))
