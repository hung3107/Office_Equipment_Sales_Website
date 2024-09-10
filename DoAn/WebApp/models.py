from django.db import models


#Create your models here.

class DanhMuc(models.Model):
    MaDanhMuc = models.IntegerField(primary_key=True)
    TenDanhMuc= models.CharField(max_length=255)

    def __str__(self):
        return self.TenDanhMuc

class SanPham(models.Model):
    MaSanPham = models.IntegerField(primary_key=True)
    TenSanPham = models.CharField(max_length=255)
    MoTa = models.TextField()
    Gia = models.FloatField()
    HinhAnhDaiDien = models.CharField(max_length=100)
    NhanHieu = models.CharField(max_length=100)
    MaDanhMuc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    TenDanhMuc= models.CharField(max_length=255)

    def __str__(self):
        return self.MaSanPham



