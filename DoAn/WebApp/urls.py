from django.urls import path
from .import views

urlpatterns = [
    path('', views.listSanPham, name='ListSanPham'),
    path('san-pham/<int:madanhmuc>/', views.listSanPham, name='listsanphamdanhmuc'),
    path('them-danh-muc/', views.themDanhMuc, name='them_danh_muc'),
    path('themsanpham/', views.themSanPham, name='themSanPham'),
    path('xoasanpham/<int:sanpham_id>/', views.xoaSanPham, name='xoaSanPham'),
]