# trong tệp models.py

from django.db import models

class Table(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self

class List(models.Model):
    title = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return self

class Card(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self
