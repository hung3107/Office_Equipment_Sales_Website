from django import forms
from .models import DanhMuc, SanPham

class DanhMucForm(forms.ModelForm):
    class Meta:
        model = DanhMuc
        fields = ['TenDanhMuc']

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['TenSanPham', 'MoTa', 'Gia', 'HinhAnhDaiDien', 'NhanHieu', 'MaDanhMuc']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Ma sản phẩm')

class DeleteProductForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
