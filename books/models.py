from django.db import models

# Create your models here.
'''Model Structure
Author--
    Book--
        Chapter 1
            Exercise 1
                solution 1
                solution 2
                ...
            Exercise 2
            ..
        Chapter 2
        ...

'''

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return f"{first_name} {last_name}"


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    isbn = models.CharField(max_length=16)
    slug = models.SlugField()
    cover = models.ImageField()
    price = models.FloatField()

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    exercise_number = models.IntegerField()
    page_number = models.IntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Solution(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{exercise} - {self.pk}"
