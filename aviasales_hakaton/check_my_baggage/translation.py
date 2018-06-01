
from modeltranslation.translator import translator, TranslationOptions

from check_my_baggage.models import AirlineCompany


class AirlineCompanyTranslationOptions(TranslationOptions):
    fields = ['name', 'description', 'baggage_allowance_link']  # logo?


translator.register(AirlineCompany, AirlineCompanyTranslationOptions)
