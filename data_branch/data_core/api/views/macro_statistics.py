from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import *
from ..serializers import *


########## Australia ##########
# Business
class AubsaigManufacturingView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = AubsaigManufacturing.objects.all()
    serializer_class = AubsaigManufacturingSerializer


class AubsaigServicesView(generics.ListAPIView):
    queryset = AubsaigServices.objects.all()
    serializer_class = AubsaigServicesSerializer


class AubsaigConstructionView(generics.ListAPIView):
    queryset = AubsaigConstruction.objects.all()
    serializer_class = AubsaigConstructionSerializer

########## USA ##########
# Business
class UsbsismmanBacklogView(generics.ListAPIView):  # ISM Manufacturing Indexes
    queryset = UsbsismmanBacklog.objects.all()
    serializer_class = UsbsismmanBacklogSerializer
class UsbsismmanCustinvView(generics.ListAPIView):
    queryset = UsbsismmanCustinv.objects.all()
    serializer_class = UsbsismmanCustinvSerializer
class UsbsismmanDelivView(generics.ListAPIView):
    queryset = UsbsismmanDeliv.objects.all()
    serializer_class = UsbsismmanDelivSerializer
class UsbsismmanEmplView(generics.ListAPIView):
    queryset = UsbsismmanEmpl.objects.all()
    serializer_class = UsbsismmanEmplSerializer
class UsbsismmanExportsView(generics.ListAPIView):
    queryset = UsbsismmanExports.objects.all()
    serializer_class = UsbsismmanExportsSerializer
class UsbsismmanImportsView(generics.ListAPIView):
    queryset = UsbsismmanImports.objects.all()
    serializer_class = UsbsismmanImportsSerializer
class UsbsismmanInventView(generics.ListAPIView):
    queryset = UsbsismmanInvent.objects.all()
    serializer_class = UsbsismmanInventSerializer
class UsbsismmanNewordersView(generics.ListAPIView):
    queryset = UsbsismmanNeworders.objects.all()
    serializer_class = UsbsismmanNewordersSerializer
class UsbsismmanPmiView(generics.ListAPIView):
    queryset = UsbsismmanPmi.objects.all()
    serializer_class = UsbsismmanPmiSerializer
class UsbsismmanPricesView(generics.ListAPIView):
    queryset = UsbsismmanPrices.objects.all()
    serializer_class = UsbsismmanPricesSerializer
class UsbsismmanProdView(generics.ListAPIView):
    queryset = UsbsismmanProd.objects.all()
    serializer_class = UsbsismmanProdSerializer

class UsbsismnmanBacklogView(generics.ListAPIView):  # ISM Non - Manufacturing Indexes
    queryset = UsbsismnmanBacklog.objects.all()
    serializer_class = UsbsismnmanBacklogSerializer
class UsbsismnmanBusactView(generics.ListAPIView):
    queryset = UsbsismnmanBusact.objects.all()
    serializer_class = UsbsismnmanBusactSerializer
class UsbsismnmanDelivView(generics.ListAPIView):
    queryset = UsbsismnmanDeliv.objects.all()
    serializer_class = UsbsismnmanDelivSerializer
class UsbsismnmanEmplView(generics.ListAPIView):
    queryset = UsbsismnmanEmpl.objects.all()
    serializer_class = UsbsismnmanEmplSerializer
class UsbsismnmanExportsView(generics.ListAPIView):
    queryset = UsbsismnmanExports.objects.all()
    serializer_class = UsbsismnmanExportsSerializer
class UsbsismnmanImportsView(generics.ListAPIView):
    queryset = UsbsismnmanImports.objects.all()
    serializer_class = UsbsismnmanImportsSerializer
class UsbsismnmanInventView(generics.ListAPIView):
    queryset = UsbsismnmanInvent.objects.all()
    serializer_class = UsbsismnmanInventSerializer
class UsbsismnmanInvsentView(generics.ListAPIView):
    queryset = UsbsismnmanInvsent.objects.all()
    serializer_class = UsbsismnmanInvsentSerializer
class UsbsismnmanNewordView(generics.ListAPIView):
    queryset = UsbsismnmanNeword.objects.all()
    serializer_class = UsbsismnmanNewordSerializer
class UsbsismnmanPmiView(generics.ListAPIView):
    queryset = UsbsismnmanPmi.objects.all()
    serializer_class = UsbsismnmanPmiSerializer
class UsbsismnmanPricesView(generics.ListAPIView):
    queryset = UsbsismnmanPrices.objects.all()
    serializer_class = UsbsismnmanPricesSerializer

class UsbsmarkitCompositeView(generics.ListAPIView):  # Markit PMIndexes
    queryset = UsbsmarkitComposite.objects.all()
    serializer_class = UsbsmarkitCompositeSerializer
class UsbsmarkitManufacturingView(generics.ListAPIView):
    queryset = UsbsmarkitManufacturing.objects.all()
    serializer_class = UsbsmarkitManufacturingSerializer
class UsbsmarkitServicesView(generics.ListAPIView):
    queryset = UsbsmarkitServices.objects.all()
    serializer_class = UsbsmarkitServicesSerializer


# Consumers
class UscscbConsumerConfidenceView(generics.ListAPIView): # CB Consumers Survey
    queryset = UscscbConsumerConfidence.objects.all()
    serializer_class = UscscbConsumerConfidenceSerializer
class UscscbExpectationsView(generics.ListAPIView):
    queryset = UscscbExpectations.objects.all()
    serializer_class = UscscbExpectationsSerializer
class UscscbPresentSituationView(generics.ListAPIView):
    queryset = UscscbPresentSituation.objects.all()
    serializer_class = UscscbPresentSituationSerializer

class UscsuomCurrentView(generics.ListAPIView):  # Uni Of Michigan Consumers Survey
    queryset = UscsuomCurrent.objects.all()
    serializer_class = UscsuomCurrentSerializer
class UscsuomExpectationsView(generics.ListAPIView):
    queryset = UscsuomExpectations.objects.all()
    serializer_class = UscsuomExpectationsSerializer
class UscsuomFiveyearinfexView(generics.ListAPIView):
    queryset = UscsuomFiveyearinfex.objects.all()
    serializer_class = UscsuomFiveyearinfexSerializer
class UscsuomOneyearinfexView(generics.ListAPIView):
    queryset = UscsuomOneyearinfex.objects.all()
    serializer_class = UscsuomOneyearinfexSerializer
class UscsuomSentimentView(generics.ListAPIView):
    queryset = UscsuomSentiment.objects.all()
    serializer_class = UscsuomSentimentSerializer


# GDP account
class UsggdpmanuView(generics.ListAPIView):  # GDP Monthly Figures
    queryset = Usggdpmanu.objects.all()
    serializer_class = UsggdpmanuSerializer
class UsggdpmdolView(generics.ListAPIView):
    queryset = Usggdpmdol.objects.all()
    serializer_class = UsggdpmdolSerializer
class UsggdpmqoqView(generics.ListAPIView):
    queryset = Usggdpmqoq.objects.all()
    serializer_class = UsggdpmqoqSerializer
class UsggdpmyoyView(generics.ListAPIView):
    queryset = Usggdpmyoy.objects.all()
    serializer_class = UsggdpmyoySerializer

class UsggdpqanuView(generics.ListAPIView):  # GDP Quarterly Figures
    queryset = Usggdpqanu.objects.all()
    serializer_class = UsggdpqanuSerializer
class UsggdpqdolView(generics.ListAPIView):
    queryset = Usggdpqdol.objects.all()
    serializer_class = UsggdpqdolSerializer
class UsggdpqqoqView(generics.ListAPIView):
    queryset = Usggdpqqoq.objects.all()
    serializer_class = UsggdpqqoqSerializer
class UsggdpqyoyView(generics.ListAPIView):
    queryset = Usggdpqyoy.objects.all()
    serializer_class = UsggdpqyoySerializer


# Inflation
class UsicocpimindView(generics.ListAPIView):  # Core inflation CPI
    queryset = Usicocpimind.objects.all()
    serializer_class = UsicocpimindSerializer
class UsicocpimmomView(generics.ListAPIView):
    queryset = Usicocpimmom.objects.all()
    serializer_class = UsicocpimmomSerializer
class UsicocpimyoyView(generics.ListAPIView):
    queryset = Usicocpimyoy.objects.all()
    serializer_class = UsicocpimyoySerializer

class UsicopcepimindView(generics.ListAPIView):  # Core inflation PCE
    queryset = Usicopcepimind.objects.all()
    serializer_class = UsicopcepimindSerializer
class UsicopcepimmomView(generics.ListAPIView):
    queryset = Usicopcepimmom.objects.all()
    serializer_class = UsicopcepimmomSerializer
class UsicopcepimyoyView(generics.ListAPIView):
    queryset = Usicopcepimyoy.objects.all()
    serializer_class = UsicopcepimyoySerializer

class UsicoppimindView(generics.ListAPIView):  # Core inflation PPI
    queryset = Usicoppimind.objects.all()
    serializer_class = UsicoppimindSerializer
class UsicoppimmomView(generics.ListAPIView):
    queryset = Usicoppimmom.objects.all()
    serializer_class = UsicoppimmomSerializer
class UsicoppimyoyView(generics.ListAPIView):
    queryset = Usicoppimyoy.objects.all()
    serializer_class = UsicoppimyoySerializer

class UsicpimindView(generics.ListAPIView):  # Inflation CPI
    queryset = Usicpimind.objects.all()
    serializer_class = UsicpimindSerializer
class UsicpimmomView(generics.ListAPIView):
    queryset = Usicpimmom.objects.all()
    serializer_class = UsicpimmomSerializer
class UsicpimyoyView(generics.ListAPIView):
    queryset = Usicpimyoy.objects.all()
    serializer_class = UsicpimyoySerializer

class UsipcepimindView(generics.ListAPIView):  # Inflation PCE
    queryset = Usipcepimind.objects.all()
    serializer_class = UsipcepimindSerializer
class UsipcepimmomView(generics.ListAPIView):
    queryset = Usipcepimmom.objects.all()
    serializer_class = UsipcepimmomSerializer
class UsipcepimyoyView(generics.ListAPIView):
    queryset = Usipcepimyoy.objects.all()
    serializer_class = UsipcepimyoySerializer

class UsippimindView(generics.ListAPIView):  # Inflation PPI
    queryset = Usippimind.objects.all()
    serializer_class = UsippimindSerializer
class UsippimmomView(generics.ListAPIView):
    queryset = Usippimmom.objects.all()
    serializer_class = UsippimmomSerializer
class UsippimyoyView(generics.ListAPIView):
    queryset = Usippimyoy.objects.all()
    serializer_class = UsippimyoySerializer

class UsiexportpimindView(generics.ListAPIView):  # Export Price Index
    queryset = Usiexportpimind.objects.all()
    serializer_class = UsiexportpimindSerializer
class UsiexportpimmomView(generics.ListAPIView):
    queryset = Usiexportpimmom.objects.all()
    serializer_class = UsiexportpimmomSerializer
class UsiexportpimyoyView(generics.ListAPIView):
    queryset = Usiexportpimyoy.objects.all()
    serializer_class = UsiexportpimyoySerializer

class UsiimportpimindView(generics.ListAPIView):  # Import Price Index
    queryset = Usiimportpimind.objects.all()
    serializer_class = UsiimportpimindSerializer
class UsiimportpimmomView(generics.ListAPIView):
    queryset = Usiimportpimmom.objects.all()
    serializer_class = UsiimportpimmomSerializer
class UsiimportpimyoyView(generics.ListAPIView):
    queryset = Usiimportpimyoy.objects.all()
    serializer_class = UsiimportpimyoySerializer

class UsigdpctpimanuView(generics.ListAPIView):  # GDP Price Index
    queryset = Usigdpctpimanu.objects.all()
    serializer_class = UsigdpctpimanuSerializer
class UsigdpctpiqanuView(generics.ListAPIView):
    queryset = Usigdpctpiqanu.objects.all()
    serializer_class = UsigdpctpiqanuSerializer

class UsihpimindView(generics.ListAPIView):  # House Price Index
    queryset = Usihpimind.objects.all()
    serializer_class = UsihpimindSerializer
class UsihpimmomView(generics.ListAPIView):
    queryset = Usihpimmom.objects.all()
    serializer_class = UsihpimmomSerializer
class UsihpimyoyView(generics.ListAPIView):
    queryset = Usihpimyoy.objects.all()
    serializer_class = UsihpimyoySerializer


# Monetary
class UsmfedrateView(generics.ListAPIView):  # FED Rate
    queryset = Usmfedrate.objects.all()
    serializer_class = UsmfedrateSerializer
