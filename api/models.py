from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    launched_on = models.DateField()
    directed_by = models.ForeignKey(
        Person, on_delete=models.PROTECT, related_name="movies_directed"
    )

    def __str__(self):
        return self.title
