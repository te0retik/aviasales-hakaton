
from django.db import models

from filer.fields.image import FilerImageField


class AirlineCompany(models.Model):
    BAGGAGE_ALLOWANCE_LINK_CROP_VIEW_LEN = 20

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
        return 'AirlineCompany(%s, %s, %sx%sx%s, %s)' % (
            self.name, self.code, self.carryon_max_x, self.carryon_max_y,
            self.carryon_max_z, self.baggage_3dimensions)

    def icon_img(self):
        url = None
        if self.icon:
            url = self.icon.url
            if self.icon.thumbnails:
                # admin_clipboard_icon, admin_directory_listing_icon
                # admin_sidebar_preview, admin_tiny_icon
                url = self.icon.thumbnails.get('admin_tiny_icon')
                if not url:
                    url = self.icon.thumbnails.get('admin_directory_listing_icon')
                if not url:
                    url = self.icon.thumbnails.get('admin_sidebar_preview')

        return '<img src="%s"/>' % url if url else ''
    icon_img.short_description = 'icon'
    icon_img.allow_tags = True

    def baggage_allowance_link_href(self):
        if len(self.baggage_allowance_link) > self.BAGGAGE_ALLOWANCE_LINK_CROP_VIEW_LEN:
            link_cropped = self.baggage_allowance_link[:self.BAGGAGE_ALLOWANCE_LINK_CROP_VIEW_LEN] + '...'
        else:
            link_cropped = self.baggage_allowance_link
        return '<a href="%s">%s</a>' % (self.baggage_allowance_link, link_cropped)
    baggage_allowance_link_href.short_description = 'icon'
    baggage_allowance_link_href.allow_tags = True
