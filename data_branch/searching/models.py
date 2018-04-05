from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ChartType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Indicator(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    chart_type = models.ForeignKey(ChartType, on_delete=models.CASCADE)
    api_url = models.CharField(max_length=200)
    name = models.CharField(max_length=65)
    description = models.TextField()
    admin_description = models.TextField(null=True)

    class Meta:
        unique_together = ('category', 'country', 'name')

    def __str__(self):
        return self.name
