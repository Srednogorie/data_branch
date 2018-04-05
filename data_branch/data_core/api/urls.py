from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from data_core.api import views

# router = routers.DefaultRouter()
# router.register('aubsaigconstruction', views.AubsaigConstructionViewSet)
app_name = "data_core"

urlpatterns = [
    # MACRO STATISTICS CATEGORY
    ########## AUSTRALIA ##########
    ##### Business #####
    url(r'^aubsaigmanufacturing/$', views.AubsaigManufacturingView.as_view(), name='aubsaigmanufacturing_list'),
    url(r'^aubsaigservices/$', views.AubsaigServicesView.as_view(), name='aubsaigservices_list'),
    url(r'^aubsaigconstruction/$', views.AubsaigConstructionView.as_view(), name='aubsaigconstruction_list'),

    ########## USA ##########
    ##### Business #####
    url(r'^usbsismmanbacklog/$', views.UsbsismmanBacklogView.as_view(), name='usbsismmanbacklog_list'),
    # ISM Manufacturing Indexes
    url(r'^usbsismmancustinv/$', views.UsbsismmanCustinvView.as_view(), name='usbsismmancustinv_list'),
    url(r'^usbsismmandeliv/$', views.UsbsismmanDelivView.as_view(), name='usbsismmandeliv_list'),
    url(r'^usbsismmanempl/$', views.UsbsismmanEmplView.as_view(), name='usbsismmanempl_list'),
    url(r'^usbsismmanexports/$', views.UsbsismmanExportsView.as_view(), name='usbsismmanexports_list'),
    url(r'^usbsismmanimports/$', views.UsbsismmanImportsView.as_view(), name='usbsismmanimports_list'),
    url(r'^usbsismmaninvent/$', views.UsbsismmanInventView.as_view(), name='usbsismmaninvent_list'),
    url(r'^usbsismmanneworders/$', views.UsbsismmanNewordersView.as_view(), name='usbsismmanneworders_list'),
    url(r'^usbsismmanpmi/$', views.UsbsismmanPmiView.as_view(), name='usbsismmanpmi_list'),
    url(r'^usbsismmanprices/$', views.UsbsismmanPricesView.as_view(), name='usbsismmanprices_list'),
    url(r'^usbsismmanprod/$', views.UsbsismmanProdView.as_view(), name='usbsismmanprod_list'),
    # ISM Non - Manufacturing Indexes
    url(r'^usbsismnmanbacklog/$', views.UsbsismnmanBacklogView.as_view(), name='usbsismnmanbacklog_list'),
    url(r'^usbsismnmanbusact/$', views.UsbsismnmanBusactView.as_view(), name='usbsismnmanbusact_list'),
    url(r'^usbsismnmandeliv/$', views.UsbsismnmanDelivView.as_view(), name='usbsismnmandeliv_list'),
    url(r'^usbsismnmanempl/$', views.UsbsismnmanEmplView.as_view(), name='usbsismnmanempl_list'),
    url(r'^usbsismnmanexports/$', views.UsbsismnmanExportsView.as_view(), name='usbsismnmanexports_list'),
    url(r'^usbsismnmanimports/$', views.UsbsismnmanImportsView.as_view(), name='usbsismnmanimports_list'),
    url(r'^usbsismnmaninvent/$', views.UsbsismnmanInventView.as_view(), name='usbsismnmaninvent_list'),
    url(r'^usbsismnmaninvsent/$', views.UsbsismnmanInvsentView.as_view(), name='usbsismnmaninvsent_list'),
    url(r'^usbsismnmanneword/$', views.UsbsismnmanNewordView.as_view(), name='usbsismnmanneword_list'),
    url(r'^usbsismnmanpmi/$', views.UsbsismnmanPmiView.as_view(), name='usbsismnmanpmi_list'),
    url(r'^usbsismnmanprices/$', views.UsbsismnmanPricesView.as_view(), name='usbsismnmanprices_list'),
    # Markit PMIndexes
    url(r'^usbsmarkitcomposite/$', views.UsbsmarkitCompositeView.as_view(), name='usbsmarkitcomposite_list'),
    url(r'^usbsmarkitmanufacturing/$', views.UsbsmarkitManufacturingView.as_view(),
        name='usbsmarkitmanufacturing_list'),
    url(r'^usbsmarkitservices/$', views.UsbsmarkitServicesView.as_view(), name='usbsmarkitservices_list'),

    ##### Consumers #####
    # CB Consumer Survey
    url(r'^uscscbconsumerconfidence/$', views.UscscbConsumerConfidenceView.as_view(),
        name='uscscbconsumerconfidence_list'),
    url(r'^uscscbexpectations/$', views.UscscbExpectationsView.as_view(), name='uscscbexpectations_list'),
    url(r'^uscscbpresentsituation/$', views.UscscbPresentSituationView.as_view(), name='uscscbpresentsituation_list'),
    # Uni Of Michigan Consumer Survey
    url(r'^uscsuomcurrent/$', views.UscsuomCurrentView.as_view(), name='uscsuomcurrent_list'),
    url(r'^uscsuomexpectations/$', views.UscsuomExpectationsView.as_view(), name='uscsuomexpectations_list'),
    url(r'^uscsuomfiveyearinfex/$', views.UscsuomFiveyearinfexView.as_view(), name='uscsuomfiveyearinfex_list'),
    url(r'^uscsuomoneyearinfex/$', views.UscsuomOneyearinfexView.as_view(), name='uscsuomoneyearinfex_list'),
    url(r'^uscsuomsentiment/$', views.UscsuomSentimentView.as_view(), name='uscsuomsentiment_list'),

    ##### GDP account #####
    # GDP Monthly Figures
    url(r'^usggdpmanu/$', views.UsggdpmanuView.as_view(), name='usggdpmanu_list'),
    url(r'^usggdpmdol/$', views.UsggdpmdolView.as_view(), name='usggdpmdol_list'),
    url(r'^usggdpmqoq/$', views.UsggdpmqoqView.as_view(), name='usggdpmqoq_list'),
    url(r'^usggdpmyoy/$', views.UsggdpmyoyView.as_view(), name='usggdpmyoy_list'),
    # GDP Quarterly Figures
    url(r'^usggdpqanu/$', views.UsggdpqanuView.as_view(), name='usggdpqanu_list'),
    url(r'^usggdpqdol/$', views.UsggdpqdolView.as_view(), name='usggdpqdol_list'),
    url(r'^usggdpqqoq/$', views.UsggdpqqoqView.as_view(), name='usggdpqqoq_list'),
    url(r'^usggdpqyoy/$', views.UsggdpqyoyView.as_view(), name='usggdpqyoy_list'),

    ##### Inflation #####
    # Core inflation CPI
    url(r'^usicocpimind/$', views.UsicocpimindView.as_view(), name='usicocpimind_list'),
    url(r'^usicocpimmom/$', views.UsicocpimmomView.as_view(), name='usicocpimmom_list'),
    url(r'^usicocpimyoy/$', views.UsicocpimyoyView.as_view(), name='usicocpimyoy_list'),
    # Core inflation PCE
    url(r'^usicopcepimind/$', views.UsicopcepimindView.as_view(), name='usicopcepimind_list'),
    url(r'^usicopcepimmom/$', views.UsicopcepimmomView.as_view(), name='usicopcepimmom_list'),
    url(r'^usicopcepimyoy/$', views.UsicopcepimyoyView.as_view(), name='usicopcepimyoy_list'),
    # Core inflation PPI
    url(r'^usicoppimind/$', views.UsicoppimindView.as_view(), name='usicoppimind_list'),
    url(r'^usicoppimmom/$', views.UsicoppimmomView.as_view(), name='usicoppimmom_list'),
    url(r'^usicoppimyoy/$', views.UsicoppimyoyView.as_view(), name='usicoppimyoy_list'),
    # Inflation CPI
    url(r'^usicpimind/$', views.UsicpimindView.as_view(), name='usicpimind_list'),
    url(r'^usicpimmom/$', views.UsicpimmomView.as_view(), name='usicpimmom_list'),
    url(r'^usicpimyoy/$', views.UsicpimyoyView.as_view(), name='usicpimyoy_list'),
    # Inflation PCE
    url(r'^usipcepimind/$', views.UsipcepimindView.as_view(), name='usipcepimind_list'),
    url(r'^usipcepimmom/$', views.UsipcepimmomView.as_view(), name='usipcepimmom_list'),
    url(r'^usipcepimyoy/$', views.UsipcepimyoyView.as_view(), name='usipcepimyoy_list'),
    # Inflation PPI
    url(r'^usippimind/$', views.UsippimindView.as_view(), name='usippimind_list'),
    url(r'^usippimmom/$', views.UsippimmomView.as_view(), name='usippimmom_list'),
    url(r'^usippimyoy/$', views.UsippimyoyView.as_view(), name='usippimyoy_list'),
    # Export Price Index
    url(r'^usiexportpimind/$', views.UsiexportpimindView.as_view(), name='usiexportpimind_list'),
    url(r'^usiexportpimmom/$', views.UsiexportpimmomView.as_view(), name='usiexportpimmom_list'),
    url(r'^usiexportpimyoy/$', views.UsiexportpimyoyView.as_view(), name='usiexportpimyoy_list'),
    # Import Price Index
    url(r'^usiimportpimind/$', views.UsiimportpimindView.as_view(), name='usiimportpimind_list'),
    url(r'^usiimportpimmom/$', views.UsiimportpimmomView.as_view(), name='usiimportpimmom_list'),
    url(r'^usiimportpimyoy/$', views.UsiimportpimyoyView.as_view(), name='usiimportpimyoy_list'),
    # GDP Price Index
    url(r'^usigdpctpimanu/$', views.UsigdpctpimanuView.as_view(), name='usigdpctpimanu_list'),
    url(r'^usigdpctpiqanu/$', views.UsigdpctpiqanuView.as_view(), name='usigdpctpiqanu_list'),
    # House Price Index
    url(r'^usihpimind/$', views.UsihpimindView.as_view(), name='usihpimind_list'),
    url(r'^usihpimmom/$', views.UsihpimmomView.as_view(), name='usihpimmom_list'),
    url(r'^usihpimyoy/$', views.UsihpimyoyView.as_view(), name='usihpimyoy_list'),

    ##### Monetary #####
    url(r'^usmfedrate/$', views.UsmfedrateView.as_view(), name='usmfedrate_list'),  # FED Rate

    # MACRO COMPARISON CATEGORY

    # MACRO TRENDS CATEGORY
    url(r'^aubsaigtrend/$', views.AustraliaAigTrend.as_view(), name='aubsaigtrend_list'),
    # # Test templates folder
    # url(r'^map/$', TemplateView.as_view(template_name='tests/map.html')),
    # url(r'^bulgaria/$', TemplateView.as_view(template_name='tests/bulgaria.html')),
    # url(r'^part1/$', TemplateView.as_view(template_name='tests/part1.html')),
    # url(r'^googlemaps/$', TemplateView.as_view(template_name='tests/googlemaps.html')),
    # #url(r'^', include(router.urls)),
    #
    # # Maps examples and functionality
    # url(r'^arc-in-center/$', TemplateView.as_view(template_name='datamaps/examples/arc-in-center.html')),
    # url(r'^arc-with-popup/$', TemplateView.as_view(template_name='datamaps/examples/arc-with-popup.html')),
    # url(r'^bubble-in-center/$', TemplateView.as_view(template_name='datamaps/examples/bubble-in-center.html')),
    # url(r'^bubble-in-center-world/$', TemplateView.as_view(template_name='datamaps/examples/bubble-in-center-world.html')),
    # url(r'^bubbles-with-shadows/$', TemplateView.as_view(template_name='datamaps/examples/bubble-with-shadows.html')),
    # url(r'^custom-labels/$', TemplateView.as_view(template_name='datamaps/examples/custom-labels.html')),
    # url(r'^custom-map-data/$', TemplateView.as_view(template_name='datamaps/examples/custom-map-data.html')),
    # url(r'^custom-map-data-multi-layer/$', TemplateView.as_view(template_name='datamaps/examples/custom-map-data-multi-layer.html')),
    # url(r'^disable-bubble-animation/$', TemplateView.as_view(template_name='datamaps/examples/disable-bubble-animation.html')),
    # url(r'^function-values/$', TemplateView.as_view(template_name='datamaps/examples/function-values.html')),
    # url(r'^graticule/$', TemplateView.as_view(template_name='datamaps/examples/graticule.html')),
    # url(r'^great-arc/$', TemplateView.as_view(template_name='datamaps/examples/great-arc.html')),
    # url(r'^hi-res/$', TemplateView.as_view(template_name='datamaps/examples/hi-res.html')),
    # url(r'^hidehawaiiandalaska/$', TemplateView.as_view(template_name='datamaps/examples/hideHawaiiAndAlaska.html')),
    # url(r'^highmaps_world/$', TemplateView.as_view(template_name='datamaps/examples/highmaps_world.html')),
    # url(r'^italy/$', TemplateView.as_view(template_name='datamaps/examples/italy.html')),
    # url(r'^remote-data/$', TemplateView.as_view(template_name='datamaps/examples/remote-data.html')),
    # url(r'^responsive/$', TemplateView.as_view(template_name='datamaps/examples/responsive.html')),
    # url(r'^test/$', TemplateView.as_view(template_name='datamaps/examples/test.html')),
    # url(r'^update-choropleth/$', TemplateView.as_view(template_name='datamaps/examples/update-choropleth.html')),
    # url(r'^update-choropleth-reset/$', TemplateView.as_view(template_name='datamaps/examples/update-choropleth-reset.html')),
    # url(r'^zoom-and-scale/$', TemplateView.as_view(template_name='datamaps/examples/zoom-and-scale.html')),
]

# This is only required to support extension-style formats (e.g. /data.csv)
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns)
