from django.db import models


class Block(models.Model):
    height = models.CharField(max_length=64, null=True)
    hash = models.CharField(max_length=64, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=64, null=True)
    count_of_transactions = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.height
