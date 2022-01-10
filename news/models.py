from django.db import models


class Article(models.Model):
    class Meta:
        ordering = ('-publish_date',)

    title = models.CharField(max_length=255)
    publish_date = models.DateField()

    body = models.TextField()
    preview_body = models.TextField()

    img_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

