"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

######################
# Veritabanına girilecek olan verileri csv dosyasından okuyup veritabanına aktarabilmek için
# geçici olarak bir kod bloğu oluşturuldu
""" import csv
from core.models import SampleApps, SampleScreenshots
from datetime import datetime

with open('static/csv/sample_apps.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    # Header'ı veritabanına aktarmayacağımızdan dolayı iteratör 
    # bir sonraki satırdan başlatıldı
    next(reader, None)
    for row in reader:
        SampleApps.objects.get_or_create(
            id=row[0],
            name=row[1],
            icon=row[2],
        )

with open('static/csv/sample_screeshots.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    # Header'ı veritabanına aktarmayacağımızdan dolayı iteratör 
    # bir sonraki satırdan başlatıldı
    next(reader, None)
    for row in reader:
        SampleScreenshots.objects.get_or_create(
            id=row[0],
            app_id=row[1],
            file_name=row[2],         
        ) """
######################
