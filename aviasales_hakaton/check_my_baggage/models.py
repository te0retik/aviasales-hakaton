
from django.db import models

from filer.fields.image import FilerImageField


class AirlineCompany(models.Model):
    name = models.CharField(verbose_name='Name', max_length=1024)
    code = models.CharField(verbose_name='IATA 2 chars code', max_length=2, db_index=True)
    icon = FilerImageField(verbose_name='Logo icon 50x50', related_name='icon', blank=True, null=True)
    logo = FilerImageField(verbose_name='Logo image [large]', related_name='logo', blank=True, null=True)
    description = models.TextField(verbose_name='Decription')
    baggage_allowance_link = models.URLField(verbose_name='Baggage allowance link')

    carryon_max_x = models.FloatField(verbose_name='Carryon max length')
    carryon_max_y = models.FloatField(verbose_name='Carryon max width')
    carryon_max_z = models.FloatField(verbose_name='Carryon max height')

    baggage_3dimensions = models.FloatField(verbose_name='Max value for the sum of 3 dimensions')

    class Meta:
        ordering = ('name', 'code')
        verbose_name = 'Airline company'
        verbose_name_plural = 'Airline companies'

    def __str__(self):
        return f'AirlineCompany({self.name}, {self.code},' \
               f' {self.carryon_max_x}x{self.carryon_max_y}x{self.carryon_max_z}),' \
               f' {self.baggage_3dimensions}'
