from django.db import models

STATUS = (
        ("new", "new"),
        ("doing", "doing"),
        ("done", "done")
    )

BOOL = (
        ("false", "false"),
        ("true", "true")
    )

class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    comment = models.TextField(default='')
    status = models.CharField(max_length=6, choices=STATUS, default='new')
    hot = models.CharField(max_length=6, choices=BOOL, default='true')

    def __str__(self):
        return self.title