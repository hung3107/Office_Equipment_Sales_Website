from django.shortcuts import render,redirect
from .models import SanPham, DanhMuc
from .forms import DanhMucForm
from .forms import SanPhamForm
from .forms import SearchForm

def listSanPham(request, madanhmuc=None):
    sanpham = SanPham.objects.all()
    danhmucsanpham = DanhMuc.objects.all()

    # Filter by category if madanhmuc is provided
    if madanhmuc:
        sanpham = sanpham.filter(MaDanhMuc_id=madanhmuc)

    # Filter by search query
    search_query = request.GET.get('q')
    if search_query:
        sanpham = sanpham.filter(TenSanPham__icontains=search_query)

    data = {
        'listsanpham': sanpham,
        'danhmucsanpham': danhmucsanpham,
        'select_madanhmuc': madanhmuc
    }
    return render(request, 'page/listSanPham.html', data)
def themDanhMuc(request):
    if request.method == 'POST':
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or homepage
            return redirect('ListSanPham')  # Change 'home' to the name of your homepage URL
    else:
        form = DanhMucForm()
    return render(request, 'page/themDanhMuc.html', {'form': form})


def themSanPham(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listSanPham')
    else:
        form = SanPhamForm()
    return render(request, 'page/themSanPham.html', {'form': form})

def xoaSanPham(request, sanpham_id):
    if request.method == 'POST':
        # Xử lý xóa sản phẩm
        sanpham = SanPham.objects.get(pk=sanpham_id)
        sanpham.delete()
        # Sau khi xóa xong, bạn có thể chuyển hướng đến trang khác hoặc cùng trang này
        return redirect('listSanPham')

