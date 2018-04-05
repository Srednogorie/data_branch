from django.contrib import admin
from .models import Category, Country, Indicator


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)


class IndicatorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Indicator, IndicatorAdmin)
