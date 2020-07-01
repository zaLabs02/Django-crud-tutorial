from django.db import models

# Create your models here.
class Data_mahasiswa(models.Model):
    npm = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'dt_mahasiswa'