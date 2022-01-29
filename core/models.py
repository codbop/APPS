from django.db import models

# Kullanıcı tablosu. Login sayfasında kullanıcıyı authenticate edebilmek için oluşturuldu.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class SampleApps(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

class SampleScreenshots(models.Model):
    app = models.ForeignKey(SampleApps, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)