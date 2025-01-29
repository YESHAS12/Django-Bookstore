from django.db import models
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new instance
            if Book.objects.filter(title=self.title, author=self.author, published_date=self.published_date).exists():
                raise ValidationError('A book with the same title, author, and published date already exists.')
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
