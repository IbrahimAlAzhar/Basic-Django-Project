from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    salary = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return self.name # in every places like admin or other places this model return the name of employee
