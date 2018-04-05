from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.mail import send_mail, BadHeaderError
import json
from django.contrib import messages
from .models import Category, Country, Indicator, ChartType
from .forms import ContactForm


# Create your views here.

def home_view(request):
    if request.method == 'GET':
        form = ContactForm()
        categories = Category.objects.all()
        first_load_indicator = Indicator.objects.get(pk=6)
        messages.add_message(request, messages.INFO, 'Hello world.')
        return render(request, 'base.html', {'categories': categories,
                                             'first_load_indicator': first_load_indicator, 'form': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']
            email = request.POST['email']
            try:
                send_mail(subject, message, email, ['thedatabranch@gmail.com'])
                return JsonResponse({"message": "Your message was sent successfully", 'form': form.errors.as_json()},
                                    content_type="application/json")
            except BadHeaderError:
                return JsonResponse({"message": "Error", 'form': form.errors}, content_type="application/json")
        else:
            return JsonResponse({'message': 'Your form is no tvalid', 'form': form.errors.as_json()}, content_type="application/json")


def ajax_search(request):
    dropdown_id = request.GET['dropdown_id']
    value_id = request.GET['value_id']
    try:
        category = request.GET['category']
    except:
        pass
    if dropdown_id == 'FormSelectCategory':
        query = Country.objects.filter(indicator__category=value_id).distinct()
        response = serializers.serialize("json", query)
    elif dropdown_id == 'FormSelectCountry':
        query = Indicator.objects.filter(country=value_id).filter(category=category)
        response = serializers.serialize("json", query)  # Serialize querySet
    return HttpResponse(response, content_type='application/json')


def ajax_determine(request):
    catry_text = request.GET['catry_text']
    catry_id = request.GET['catry_id']
    country_text = request.GET['country_text']
    country_id = request.GET['country_id']
    indtr_text = request.GET['indtr_text']
    indtr_id = request.GET['indtr_id']

    indicator_query = Indicator.objects.get(pk=indtr_id)
    chart_type = ChartType.objects.get(name=indicator_query.chart_type)

    response = serializers.serialize('json', [indicator_query])  # Serialize single object

    data = {
        'response': response,
        'chart_type': chart_type
    }
    # return HttpResponse(data, content_type='application/json') # Send the response as array from serialize
    # No need to use JSON.parse at the front
    return HttpResponse(json.dumps(data))  # As there are more vars that need to be added to the response
    # combine all in an dict, dump it and send it as JSON


def ajax_charts_initial(request):
    indctr_pk = request.POST['inditr_pk']
    initial_chart = Indicator.objects.get(pk=indctr_pk)
    chart_type = ChartType.objects.get(name=initial_chart.chart_type)
    return render(request, 'dummy.html', {'chart_type': chart_type, 'data_url': initial_chart.api_url,
                                          'chart_name': initial_chart.name,
                                          'chart_description': initial_chart.description})
