from django.db import models

# Kullanıcı tablosu. Login sayfasında kullanıcıyı authenticate edebilmek için oluşturuldu.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)