import pandas as pd
from data_core.models import AubsaigTrend, AubsaigManufacturing, AubsaigServices, AubsaigConstruction



def aubsaig_update():
    man = AubsaigManufacturing.objects.all()
    ser = AubsaigServices.objects.all()
    cons = AubsaigConstruction.objects.all()
