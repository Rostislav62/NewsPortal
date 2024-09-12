from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.CharField(max_length=100)
    type = models.BooleanField()  # Новое поле с типом Boolean которое показывает что это статья type=False

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.CharField(max_length=100)
    type = models.BooleanField()  # Новое поле с типом Boolean которое показывает что это новость type=True

    def __str__(self):
        return self.title