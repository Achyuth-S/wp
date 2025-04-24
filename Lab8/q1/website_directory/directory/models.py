from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    visits = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class General(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title