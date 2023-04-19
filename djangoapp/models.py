from django.db import models


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
