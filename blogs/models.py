from django.db import models
from django.utils.html import strip_tags


class Article(models.Model):
    class BlogStatus(models.IntegerChoices):
        DRAFT = 1
        PUBLISHED = 2

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content_image = models.ImageField(upload_to='articles/')
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=BlogStatus.choices)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    @property
    def formatted_markdown(self):
        # return strip_tags(markdownify(self.body))
        return self.body

    def snippet(self):
        return self.formatted_markdown[:150].replace('\n', ' ') + '...'


class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)
    menu_position = models.PositiveSmallIntegerField(default=0)  # if 0 status=False

    def __str__(self):
        return self.name
