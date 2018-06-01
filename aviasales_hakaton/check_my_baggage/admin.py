
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from check_my_baggage.models import AirlineCompany


class AirlineCompanyAdmin(TranslationAdmin):
    list_display = ('code', 'name', 'baggage_allowance_link', 'carryon_max_x',
                    'carryon_max_y', 'carryon_max_z', 'baggage_3dimensions')
    list_display_links = ('code',)


admin.site.register(AirlineCompany, AirlineCompanyAdmin)
