from rest_framework import serializers
from data_core.models import *

########## Australia ##########
# Business
class AubsaigManufacturingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AubsaigManufacturing
        fields = ('period', 'value')


class AubsaigServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AubsaigServices
        fields = ('period', 'value')


class AubsaigConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AubsaigConstruction
        fields = ('period', 'value')


########## USA ##########
# Business
class UsbsismmanBacklogSerializer(serializers.ModelSerializer):  # ISM Manufacturing Indexes
    class Meta:
        model = UsbsismmanBacklog
        fields = ('period', 'value')
class UsbsismmanCustinvSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanCustinv
        fields = ('period', 'value')
class UsbsismmanDelivSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanDeliv
        fields = ('period', 'value')
class UsbsismmanEmplSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanEmpl
        fields = ('period', 'value')
class UsbsismmanExportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanExports
        fields = ('period', 'value')
class UsbsismmanImportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanImports
        fields = ('period', 'value')
class UsbsismmanInventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanInvent
        fields = ('period', 'value')
class UsbsismmanNewordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanNeworders
        fields = ('period', 'value')
class UsbsismmanPmiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanPmi
        fields = ('period', 'value')
class UsbsismmanPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanPrices
        fields = ('period', 'value')
class UsbsismmanProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismmanProd
        fields = ('period', 'value')

class UsbsismnmanBacklogSerializer(serializers.ModelSerializer):  # ISM Non - Manufacturing Indexes
    class Meta:
        model = UsbsismnmanBacklog
        fields = ('period', 'value')
class UsbsismnmanBusactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanBusact
        fields = ('period', 'value')
class UsbsismnmanDelivSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanDeliv
        fields = ('period', 'value')
class UsbsismnmanEmplSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanEmpl
        fields = ('period', 'value')
class UsbsismnmanExportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanExports
        fields = ('period', 'value')
class UsbsismnmanImportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanImports
        fields = ('period', 'value')
class UsbsismnmanInventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanInvent
        fields = ('period', 'value')
class UsbsismnmanInvsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanInvsent
        fields = ('period', 'value')
class UsbsismnmanNewordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanNeword
        fields = ('period', 'value')
class UsbsismnmanPmiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanPmi
        fields = ('period', 'value')
class UsbsismnmanPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsismnmanPrices
        fields = ('period', 'value')

class UsbsmarkitCompositeSerializer(serializers.ModelSerializer):  # Markit PMIndexes
    class Meta:
        model = UsbsmarkitComposite
        fields = ('period', 'value')
class UsbsmarkitManufacturingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsmarkitManufacturing
        fields = ('period', 'value')
class UsbsmarkitServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbsmarkitServices
        fields = ('period', 'value')


# Consumers
class UscscbConsumerConfidenceSerializer(serializers.ModelSerializer): # CB Consumers Survey
    class Meta:
        model = UscscbConsumerConfidence
        fields = ('period', 'value')
class UscscbExpectationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UscscbExpectations
        fields = ('period', 'value')
class UscscbPresentSituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UscscbPresentSituation
        fields = ('period', 'value')

class UscsuomCurrentSerializer(serializers.ModelSerializer):  # Uni Of Michigan Consumers Survey
    class Meta:
        model = UscsuomCurrent
        fields = ('period', 'value')
class UscsuomExpectationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UscsuomExpectations
        fields = ('period', 'value')
class UscsuomFiveyearinfexSerializer(serializers.ModelSerializer):
    class Meta:
        model = UscsuomFiveyearinfex
        fields = ('period', 'value')
class UscsuomOneyearinfexSerializer(serializers.ModelSerializer):
    class Meta:
        model = UscsuomOneyearinfex
        fields = ('period', 'value')
class UscsuomSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UscsuomSentiment
        fields = ('period', 'value')


# GDP account
class UsggdpmanuSerializer(serializers.ModelSerializer):  # GDP Monthly Figures
    class Meta:
        model = Usggdpmanu
        fields = ('period', 'value')
class UsggdpmdolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usggdpmdol
        fields = ('period', 'value')
class UsggdpmqoqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usggdpmqoq
        fields = ('period', 'value')
class UsggdpmyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usggdpmyoy
        fields = ('period', 'value')

class UsggdpqanuSerializer(serializers.ModelSerializer):  # GDP Quarterly Figures
    class Meta:
        model = Usggdpqanu
        fields = ('period', 'value')
class UsggdpqdolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usggdpqdol
        fields = ('period', 'value')
class UsggdpqqoqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usggdpqqoq
        fields = ('period', 'value')
class UsggdpqyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usggdpqyoy
        fields = ('period', 'value')


# Inflation
class UsicocpimindSerializer(serializers.ModelSerializer):  # Core inflation CPI
    class Meta:
        model = Usicocpimind
        fields = ('period', 'value')
class UsicocpimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicocpimmom
        fields = ('period', 'value')
class UsicocpimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicocpimyoy
        fields = ('period', 'value')

class UsicopcepimindSerializer(serializers.ModelSerializer):  # Core inflation PCE
    class Meta:
        model = Usicopcepimind
        fields = ('period', 'value')
class UsicopcepimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicopcepimmom
        fields = ('period', 'value')
class UsicopcepimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicopcepimyoy
        fields = ('period', 'value')

class UsicoppimindSerializer(serializers.ModelSerializer):  # Core inflation PPI
    class Meta:
        model = Usicoppimind
        fields = ('period', 'value')
class UsicoppimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicoppimmom
        fields = ('period', 'value')
class UsicoppimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicoppimyoy
        fields = ('period', 'value')

class UsicpimindSerializer(serializers.ModelSerializer):  # Inflation CPI
    class Meta:
        model = Usicpimind
        fields = ('period', 'value')
class UsicpimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicpimmom
        fields = ('period', 'value')
class UsicpimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usicpimyoy
        fields = ('period', 'value')

class UsipcepimindSerializer(serializers.ModelSerializer):  # Inflation PCE
    class Meta:
        model = Usipcepimind
        fields = ('period', 'value')
class UsipcepimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usipcepimmom
        fields = ('period', 'value')
class UsipcepimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usipcepimyoy
        fields = ('period', 'value')

class UsippimindSerializer(serializers.ModelSerializer):  # Inflation PPI
    class Meta:
        model = Usippimind
        fields = ('period', 'value')
class UsippimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usippimmom
        fields = ('period', 'value')
class UsippimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usippimyoy
        fields = ('period', 'value')

class UsiexportpimindSerializer(serializers.ModelSerializer):  # Export Price Index
    class Meta:
        model = Usiexportpimind
        fields = ('period', 'value')
class UsiexportpimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usiexportpimmom
        fields = ('period', 'value')
class UsiexportpimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usiexportpimyoy
        fields = ('period', 'value')

class UsiimportpimindSerializer(serializers.ModelSerializer):  # Import Price Index
    class Meta:
        model = Usiimportpimind
        fields = ('period', 'value')
class UsiimportpimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usiimportpimmom
        fields = ('period', 'value')
class UsiimportpimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usiimportpimyoy
        fields = ('period', 'value')

class UsigdpctpimanuSerializer(serializers.ModelSerializer):  # GDP Price Index
    class Meta:
        model = Usigdpctpimanu
        fields = ('period', 'value')
class UsigdpctpiqanuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usigdpctpiqanu
        fields = ('period', 'value')

class UsihpimindSerializer(serializers.ModelSerializer):  # House Price Index
    class Meta:
        model = Usihpimind
        fields = ('period', 'value')
class UsihpimmomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usihpimmom
        fields = ('period', 'value')
class UsihpimyoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usihpimyoy
        fields = ('period', 'value')


# Monetary
class UsmfedrateSerializer(serializers.ModelSerializer):  # FED Rate
    class Meta:
        model = Usmfedrate
        fields = ('period', 'value')
