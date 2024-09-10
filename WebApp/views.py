from django.shortcuts import render,redirect
from .models import SanPham, DanhMuc, ChiTietSanPham, KhachHang
from .forms import DanhMucForm, SanPhamForm, DangKyForm, DangNhapForm
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login # type: ignore

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
def themDanhMuc(request, id=None):
    if id:
        danhmuc = get_object_or_404(DanhMuc, MaDanhMuc=id)
    else:
        danhmuc = None

    if request.method == 'POST':
        if 'delete' in request.POST and danhmuc:
            danhmuc.delete()
            return redirect('them_danh_muc')
        else:
            form = DanhMucForm(request.POST, instance=danhmuc)
            if form.is_valid():
                form.save()
                return redirect('them_danh_muc')
    else:
        form = DanhMucForm(instance=danhmuc)

    danhmuc_list = DanhMuc.objects.all()
    return render(request, 'page/themDanhMuc.html', {'form': form, 'danhmuc_list': danhmuc_list, 'danhmuc': danhmuc})


def index(request, madanhmuc = None):
    categories = DanhMuc.objects.all()
    search_query = request.GET.get('searchtx')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.get('category')

    products = SanPham.objects.all()

    if request.method == 'POST':
        search_query = request.POST.get('searchtxt', '')
        products = SanPham.objects.filter(TenSanPham__icontains=search_query)
    if search_query:
        products = products.filter(TenSanPham__icontains=search_query)
    if min_price:
        products = products.filter(Gia__gte=min_price)
    if max_price:
        products = products.filter(Gia__lte=max_price)
    if category:
        products = products.filter(MaDanhMuc=category)
    elif madanhmuc:
        products = SanPham.objects.filter(MaDanhMuc_id=madanhmuc)

    return render(request, 'page/index.html', {'categories': categories, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(SanPham, pk=pk)
    return render(request, 'page/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(SanPham, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})
    if str(product_id) in cart:  # Đảm bảo dùng khóa là chuỗi để nhất quán với view_cart
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {
            'product_id': product_id,
            'name': product.TenSanPham,
            'price': product.Gia,
            'quantity': quantity
        }

    request.session['cart'] = cart
    messages.success(request, f"Thêm {product.TenSanPham} vào giỏ hàng thành công!")
    return redirect('product_detail', pk=product_id)


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for item_id, item_data in cart.items():
        product = get_object_or_404(SanPham, pk=item_id)  # Lấy thông tin sản phẩm từ database
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'item_price': item_data['price'] * item_data['quantity']
        })

    total_quantity = sum(item['quantity'] for item in cart_items)
    total_price = sum(item['item_price'] for item in cart_items)

    return render(request, 'page/cart.html', {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_price': total_price
    })


def update_cart(request):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))

        product = get_object_or_404(SanPham, pk=product_id)

        cart = request.session.get('cart', {})
        cart[product_id] = {
            'product_id': product_id,
            'name': product.TenSanPham,
            'price': product.Gia,
            'quantity': quantity
        }
        request.session['cart'] = cart
        messages.success(request, f"Giỏ hàng đã được cập nhật!")
        return redirect('view_cart')


def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if str(product_id) in cart:  # đảm bảo rằng product_id là dạng chuỗi
            del cart[str(product_id)]
            request.session['cart'] = cart
            messages.success(request, "Xóa sản phẩm khỏi giỏ hàng thành công!")

    return redirect('view_cart')

def clear_cart(request):
    if request.method == 'POST' or request.method == 'GET':
        request.session['cart'] = {}

    return redirect('view_cart')

def admin_layout(request):
    return render(request, 'page/layoutAdmin.html')

def loai_san_pham(request):
    form = DanhMucForm()
    if request.method == 'POST':
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dsLoaiSanPham')  # type: ignore # Thay thế bằng URL tương ứng của bạn
    else:
       data = {
            'form':form,
            'WebApp_danhmuc' : DanhMuc.objects.all(),
       }
    return render(request, 'page/LoaiSanPham.html', data)

def DangKy(request):
    if request.method == 'POST':
        form = DangKyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dangnhap')
    else:
        form = DangKyForm()
    return render(request, 'page/DangKyAccount.html', {'form': form})

def dang_nhap(request):
    if request.method == 'POST':
        form = DangNhapForm(request.POST)
        if form.is_valid():
            ten_dang_nhap = form.cleaned_data['TenDangNhap']
            mat_khau = form.cleaned_data['MatKhau']
            khach_hang = KhachHang.objects.filter(TenDangNhap=ten_dang_nhap).first()
            
            if khach_hang is not None and khach_hang.MatKhau == mat_khau:
                return redirect('/')  
            else:
                form.add_error(None, "Tên đăng nhập hoặc mật khẩu không chính xác.")
    else:
        form = DangNhapForm()
    return render(request, 'page/DangNhap.html', {'form': form})

def dskhachhang(request):
    khach_hang_list = KhachHang.objects.all()
    return render(request, 'page/DanhSachKhachHang.html', {'khach_hang_list': khach_hang_list})
def dstkkh(request):
    khach_hang_list = KhachHang.objects.all()
    return render(request, 'page/DanhSachTaiKhoanKH.html', {'khach_hang_list': khach_hang_list})
def them_san_pham(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or homepage
            return redirect('ListSanPham')  # Change 'ListSanPham' to the appropriate URL name
    else:
        form = SanPhamForm()
    return render(request, 'page/them_san_pham.html', {'form': form})