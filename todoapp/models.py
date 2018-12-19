from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 250, help_text = "The Name of the Author", default = 1)
    password = models.CharField(max_length = 100, help_text = "Password", default = 1)

    def __str__(self):
        return self.name

class Todo(models.Model):
    content = models.CharField(max_length = 1000, help_text = "Your todo", default = 1)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, blank = True, default = 1)

    def __str__(self):
        return self.content