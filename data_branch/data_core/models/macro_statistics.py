from django.db import models


# Create your models here.

class MacroStatisticsBase(models.Model):
    period = models.DateField(db_column='Period', primary_key=True)
    value = models.DecimalField(db_column='Value', max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.period

    class Meta:
        abstract = True

########## Australia ##########
# Business
class AubsaigManufacturing(MacroStatisticsBase):  # AIG PMIndexes
    pass
class AubsaigServices(MacroStatisticsBase):
    pass
class AubsaigConstruction(MacroStatisticsBase):
    pass

########## USA ##########
# Business
class UsbsismmanBacklog(MacroStatisticsBase):  # ISM Manufacturing Indexes
    pass
class UsbsismmanCustinv(MacroStatisticsBase):
    pass
class UsbsismmanDeliv(MacroStatisticsBase):
    pass
class UsbsismmanEmpl(MacroStatisticsBase):
    pass
class UsbsismmanExports(MacroStatisticsBase):
    pass
class UsbsismmanImports(MacroStatisticsBase):
    pass
class UsbsismmanInvent(MacroStatisticsBase):
    pass
class UsbsismmanNeworders(MacroStatisticsBase):
    pass
class UsbsismmanPmi(MacroStatisticsBase):
    pass
class UsbsismmanPrices(MacroStatisticsBase):
    pass
class UsbsismmanProd(MacroStatisticsBase):
    pass

class UsbsismnmanBacklog(MacroStatisticsBase):  # ISM Non - Manufacturing Indexes
    pass
class UsbsismnmanBusact(MacroStatisticsBase):
    pass
class UsbsismnmanDeliv(MacroStatisticsBase):
    pass
class UsbsismnmanEmpl(MacroStatisticsBase):
    pass
class UsbsismnmanExports(MacroStatisticsBase):
    pass
class UsbsismnmanImports(MacroStatisticsBase):
    pass
class UsbsismnmanInvent(MacroStatisticsBase):
    pass
class UsbsismnmanInvsent(MacroStatisticsBase):
    pass
class UsbsismnmanNeword(MacroStatisticsBase):
    pass
class UsbsismnmanPmi(MacroStatisticsBase):
    pass
class UsbsismnmanPrices(MacroStatisticsBase):
    pass

class UsbsmarkitComposite(MacroStatisticsBase):  # Markit PMIndexes
    pass
class UsbsmarkitManufacturing(MacroStatisticsBase):
    pass
class UsbsmarkitServices(MacroStatisticsBase):
    pass


# Consumers
class UscscbConsumerConfidence(MacroStatisticsBase): # CB Consumers Survey
    pass
class UscscbExpectations(MacroStatisticsBase):
    pass
class UscscbPresentSituation(MacroStatisticsBase):
    pass

class UscsuomCurrent(MacroStatisticsBase):  # Uni Of Michigan Consumers Survey
    pass
class UscsuomExpectations(MacroStatisticsBase):
    pass
class UscsuomFiveyearinfex(MacroStatisticsBase):
    pass
class UscsuomOneyearinfex(MacroStatisticsBase):
    pass
class UscsuomSentiment(MacroStatisticsBase):
    pass


# GDP account
class Usggdpmanu(MacroStatisticsBase):  # GDP Monthly Figures
    pass
class Usggdpmdol(MacroStatisticsBase):
    pass
class Usggdpmqoq(MacroStatisticsBase):
    pass
class Usggdpmyoy(MacroStatisticsBase):
    pass

class Usggdpqanu(MacroStatisticsBase):  # GDP Quarterly Figures
    pass
class Usggdpqdol(MacroStatisticsBase):
    pass
class Usggdpqqoq(MacroStatisticsBase):
    pass
class Usggdpqyoy(MacroStatisticsBase):
    pass


# Inflation
class Usicocpimind(MacroStatisticsBase):  # Core inflation CPI
    pass
class Usicocpimmom(MacroStatisticsBase):
    pass
class Usicocpimyoy(MacroStatisticsBase):
    pass

class Usicopcepimind(MacroStatisticsBase):  # Core inflation PCE
    pass
class Usicopcepimmom(MacroStatisticsBase):
    pass
class Usicopcepimyoy(MacroStatisticsBase):
    pass

class Usicoppimind(MacroStatisticsBase):  # Core inflation PPI
    pass
class Usicoppimmom(MacroStatisticsBase):
    pass
class Usicoppimyoy(MacroStatisticsBase):
    pass

class Usicpimind(MacroStatisticsBase):  # Inflation CPI
    pass
class Usicpimmom(MacroStatisticsBase):
    pass
class Usicpimyoy(MacroStatisticsBase):
    pass

class Usipcepimind(MacroStatisticsBase):  # Inflation PCE
    pass
class Usipcepimmom(MacroStatisticsBase):
    pass
class Usipcepimyoy(MacroStatisticsBase):
    pass

class Usippimind(MacroStatisticsBase):  # Inflation PPI
    pass
class Usippimmom(MacroStatisticsBase):
    pass
class Usippimyoy(MacroStatisticsBase):
    pass

class Usiexportpimind(MacroStatisticsBase):  # Export Price Index
    pass
class Usiexportpimmom(MacroStatisticsBase):
    pass
class Usiexportpimyoy(MacroStatisticsBase):
    pass

class Usiimportpimind(MacroStatisticsBase):  # Import Price Index
    pass
class Usiimportpimmom(MacroStatisticsBase):
    pass
class Usiimportpimyoy(MacroStatisticsBase):
    pass

class Usigdpctpimanu(MacroStatisticsBase):  # GDP Price Index
    pass
class Usigdpctpiqanu(MacroStatisticsBase):
    pass

class Usihpimind(MacroStatisticsBase):  # House Price Index
    pass
class Usihpimmom(MacroStatisticsBase):
    pass
class Usihpimyoy(MacroStatisticsBase):
    pass


# Monetary
class Usmfedrate(MacroStatisticsBase):  # FED Rate
    pass
