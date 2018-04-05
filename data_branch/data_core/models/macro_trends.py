from django.db import models


# Create your models here.

class AubsaigTrend(models.Model):
    period = models.DateField(db_column='Period', primary_key=True)
    manufacturing = models.DecimalField(db_column='Manufacturing', max_digits=12, decimal_places=2, blank=True,
                                        null=True)
    services = models.DecimalField(db_column='Services', max_digits=12, decimal_places=2, blank=True, null=True)
    construction = models.DecimalField(db_column='Construction', max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.period
