from django.db import models




from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books/images')
    average_rating = models.FloatField(default=0)
    quantity = models.PositiveBigIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name
    
   