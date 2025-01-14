# Generated by Django 5.0.4 on 2024-06-04 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChiTietSanPham',
            fields=[
                ('MaSanPham', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='WebApp.sanpham')),
                ('MauSac', models.CharField(max_length=50)),
                ('HinhAnhChiTiet', models.CharField(blank=True, max_length=1000, null=True)),
                ('SoLuong', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('MaDonHang', models.AutoField(primary_key=True, serialize=False)),
                ('NgayDatHang', models.DateField()),
                ('TongTien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DiaChiGiaoHang', models.CharField(max_length=255)),
                ('TrangThai', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('MaKhachHang', models.AutoField(primary_key=True, serialize=False)),
                ('Ten', models.CharField(max_length=100)),
                ('DiaChi', models.CharField(max_length=255)),
                ('SoDienThoai', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=255, unique=True)),
                ('TenDangNhap', models.CharField(max_length=100)),
                ('MatKhau', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChiTietDonHang',
            fields=[
                ('MaChiTietDonHang', models.AutoField(primary_key=True, serialize=False)),
                ('SoLuong', models.IntegerField()),
                ('DonGia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MaSanPham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.sanpham')),
                ('MaDonHang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.donhang')),
            ],
        ),
        migrations.AddField(
            model_name='donhang',
            name='MaKhachHang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.khachhang'),
        ),
    ]
