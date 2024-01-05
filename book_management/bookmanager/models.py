from django.db import models

# Create your models here.

class LibraryLevel(models.Model):
       level_number = models.IntegerField(unique=True)
       description = models.TextField(blank=True)
       

       def __str__(self):
           return f"Level {self.level_number}"

class Shelf(models.Model):
       level = models.ForeignKey(LibraryLevel, on_delete=models.CASCADE, related_name='shelves')
       shelf_number = models.CharField(max_length=100)
       description = models.CharField(max_length=100,default="...")
       x_coordinate = models.IntegerField(default=-1)
       y_coordinate = models.IntegerField(default=-1)
       z_coordinate = models.IntegerField(default=-1)
       location_description = models.CharField(max_length=100,default="...") #this can be like near the entrance ...
       

       class Meta:
           unique_together = ('level', 'shelf_number')

       def __str__(self):
           return f"Shelf {self.shelf_number} on {self.level}"
   



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    shelves = models.ManyToManyField('Shelf' , related_name="books")
    rating=models.FloatField()

    def __str__(self):
        return self.title



class Section(models.Model):
     level = models.ForeignKey(LibraryLevel, related_name = 'sections', on_delete=models.CASCADE)
     name  = models.CharField(max_length=100)
     description = models.TextField(blank=True)

     def __str__(self):
          return f"{self.name} (level {self.level.level_number})"
 