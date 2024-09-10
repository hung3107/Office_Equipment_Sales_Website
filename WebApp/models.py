from django.db import models

# Create your models here.

class DanhMuc(models.Model):

    MaDanhMuc = models.IntegerField(primary_key=True)
    TenDanhMuc= models.CharField(max_length=255)

class SanPham(models.Model):
    MaSanPham = models.IntegerField(primary_key=True)
    TenSanPham = models.CharField(max_length=255)
    MoTa = models.TextField();
    Gia = models.FloatField();
    HinhAnhDaiDien = models.CharField(max_length=100)
    NhanHieu = models.CharField(max_length=100)
    MaDanhMuc_id = models.IntegerField()

class ChiTietSanPham(models.Model):
    MaSanPham = models.OneToOneField(SanPham, on_delete=models.CASCADE, primary_key=True)
    MauSac = models.CharField(max_length=50)
    HinhAnhChiTiet = models.CharField(max_length=1000, blank=True, null=True)
    SoLuong = models.IntegerField()

    def __str__(self):
        return f"{self.MaSanPham.TenSanPham} - {self.MauSac}"

class KhachHang(models.Model):
    MaKhachHang = models.AutoField(primary_key=True)
    Ten = models.CharField(max_length=100)
    DiaChi = models.CharField(max_length=255)
    SoDienThoai = models.CharField(max_length=20)
    Email = models.EmailField(max_length=255, unique=True)
    TenDangNhap = models.CharField(max_length=100)
    MatKhau = models.CharField(max_length=100)

    def __str__(self):
        return self.Ten

class DonHang(models.Model):
    MaDonHang = models.AutoField(primary_key=True)
    MaKhachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayDatHang = models.DateField()
    TongTien = models.DecimalField(max_digits=10, decimal_places=2)
    DiaChiGiaoHang = models.CharField(max_length=255)
    TrangThai = models.BooleanField(default=False)

    def __str__(self):
        return str(self.MaDonHang)

class ChiTietDonHang(models.Model):
    MaChiTietDonHang = models.AutoField(primary_key=True)
    MaDonHang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    MaSanPham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SoLuong = models.IntegerField()
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.MaDonHang} - {self.MaSanPham}"
    
class Admin(models.Model):
    ID = models.AutoField(primary_key=True)
    tendangnhap = models.CharField(max_length=100)
    matkhau = models.CharField(max_length=100)

    def __str__(self):
        return self.tendangnhap