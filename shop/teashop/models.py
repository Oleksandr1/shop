from django.db import models

# Create your models here.
class Sort(models.Model):

    class Meta:
        verbose_name = "Sort"
        verbose_name_plural = "Sorts"

    name = models.CharField(max_length=256, blank=False, verbose_name='Sort')
    description = models.TextField(blank=False, verbose_name='Description')
    photo = models.ImageField(blank=True, verbose_name='Photo',)

    def __str__(self):
        return ("%s %s" % self.name)

