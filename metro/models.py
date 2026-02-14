from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class MetroLine(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
    )
    color = models.CharField(
        max_length=255,
        verbose_name=_("Color"),
        blank=True,
        null=True,
    )
    number = models.IntegerField(
        verbose_name=_("Line number"),
        null=True,
        blank=True,
    )
    icon = models.ImageField(
        upload_to="metro/",
        verbose_name=_("Icon"),
        blank=True,
        null=True,
    )

    @classmethod
    def get_all(cls):
        items = cls.objects.all()
        result = dict()
        for item in items:
            result[item.number] = item
        return result

    def get_admin_color(self):
        return format_html(
            '<div style="width: 60px; height: 20px; background: {};"></div>',
            self.color,
        )

    get_admin_color.short_description = _("Color")

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["number"]
        verbose_name = _("Metro line")
        verbose_name_plural = _("Metro lines")


class Metro(models.Model):
    line = models.ForeignKey(
        MetroLine,
        verbose_name=_("Metro line"),
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
    )
    order = models.PositiveIntegerField(
        verbose_name=_("Order"),
        default=0,
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Metro station")
        verbose_name_plural = _("Metro stations")
