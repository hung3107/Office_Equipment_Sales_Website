from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='ListSanPham'),
    path('san-pham/<int:madanhmuc>/', views.listSanPham, name='listsanphamdanhmuc'),
    path('them-danh-muc/', views.themDanhMuc, name='them_danh_muc'),
    path('danhmuc/<int:id>/', views.themDanhMuc, name='editDanhmuc'),
    path('category/<int:madanhmuc>/', views.index, name='product_by_category'),
    path('dsLoaiSanPham', views.loai_san_pham, name='dsLoaiSanPham'),
    
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('admin/', views.admin_layout, name='admin_layout'),
    path('dangky', views.DangKy, name='dang_ky'),
    path('dangnhap',views.dang_nhap,name='dangnhap'),
    path('dskhachhang/', views.dskhachhang, name='dskhachhang'),
    path('taikhoankh/', views.dstkkh, name='taikhoankh'),
    path('them_san_pham/', views.them_san_pham, name='them_san_pham')
]