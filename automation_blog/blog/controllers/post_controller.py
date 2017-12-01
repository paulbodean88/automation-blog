from ..models import Post


class PostController(object):
    @staticmethod
    def get_all():
        return Post.objects.all()

    @staticmethod
    def get_page(page_number):
        posts = Post.objects.all().order_by("-created_date")
        return posts[page_number * 3: page_number * 3 + 3]

    @staticmethod
    def count():
        return Post.objects.count()

    @staticmethod
    def has_next_page(current_page):
        if current_page * 3 + 3 >= PostController.count():
            return False
        else:
            return True
