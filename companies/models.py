from django.db import models
from django.urls import reverse
# Create your models here


class Company(models.Model):
    name = models.CharField('Company Name', max_length=120)
    location = models.URLField('URL location')
    open = models.TimeField("ex: (10:00:00)")
    close = models.TimeField("ex: (18:00:00)")
    website_address = models.URLField('website URL')
    LOCAL = 'local'
    INTERNATIONAL = 'international'
    UNKNOWN = 'unknown'
    STATUS = [
        (LOCAL, ('Local company')),
        (INTERNATIONAL, ('International company')),
        (UNKNOWN, ('Unknown')),
    ]
    company_status = models.CharField(max_length=35, choices=STATUS, default=UNKNOWN)


    def __str__(self):
        return self.name


