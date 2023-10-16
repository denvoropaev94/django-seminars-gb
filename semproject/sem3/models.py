from django.db import models
from django.utils import timezone
from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    published = models.BooleanField()

    def __str__(self):
        return f'Title is {self.title}'


class Comment(models.Model):
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment{self.comment}, date{self.date}'

    # def get_summary(self):
    #     words = self.content.split()
    #     return f'{" ".join(words[:12])}...'
