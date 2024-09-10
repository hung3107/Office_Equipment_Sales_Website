import os
from django import forms # type: ignore

from DoAn import settings # type: ignore
from .models import DanhMuc,SanPham,KhachHang
from django.core.files.storage import FileSystemStorage # type: ignore

class DanhMucForm(forms.ModelForm):
    class Meta:
        model = DanhMuc
        fields = ['TenDanhMuc']

class DangNhapForm(forms.Form):
    TenDangNhap = forms.CharField(max_length=100)
    MatKhau = forms.CharField(widget=forms.PasswordInput)


class DangKyForm(forms.ModelForm):
    MatKhau = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = KhachHang
        fields = ['Ten', 'DiaChi', 'SoDienThoai', 'Email', 'TenDangNhap', 'MatKhau']

class SanPhamForm(forms.ModelForm):  # Change models.ModelForm to forms.ModelForm
    class Meta:
        model = SanPham  # Use your model
        fields = ['MaSanPham', 'TenSanPham', 'MoTa', 'Gia', 'HinhAnhDaiDien', 'NhanHieu', 'MaDanhMuc_id']
        
    #HinhAnhDaiDien = forms.ImageField (label='Hình ảnh sản phẩm')