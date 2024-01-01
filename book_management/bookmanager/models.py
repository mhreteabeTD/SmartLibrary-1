from django.db import models

# Create your models here.

class LibraryLevel(models.Model):
       level_number = models.IntegerField(unique=True)
       description = models.TextField(blank=True)

       def __str__(self):
           return f"Level {self.level_number}"

class Shelf(models.Model):
       level = models.ForeignKey(LibraryLevel, on_delete=models.CASCADE, related_name='shelves')
       shelf_number = models.IntegerField()
       description = models.TextField(blank=True)

       class Meta:
           unique_together = ('level', 'shelf_number')

       def __str__(self):
           return f"Shelf {self.shelf_number} on {self.level}"
   



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    location = models.ForeignKey(Shelf , on_delete=models.CASCADE , related_name="books")
    rating=models.FloatField()

    def __str__(self):
        return self.title
