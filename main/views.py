from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def register_ajax(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    if password1 != password2:
        return JsonResponse({
            'status': 'error',
            'message': 'Passwords do not match'
        }, status=400)
    
    if len(password1) < 8:
        return JsonResponse({
            'status': 'error',
            'message': 'Password must be at least 8 characters'
        }, status=400)
    
    # Cek apakah username sudah ada
    from django.contrib.auth.models import User
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'status': 'error',
            'message': 'Username already exists'
        }, status=400)
    
    # Buat user baru
    try:
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Account created successfully! Please login.'
        }, status=201)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


@csrf_exempt
@require_POST
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return JsonResponse({
            'status': 'success',
            'message': 'Login successful!',
            'username': user.username
        }, status=200)
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid username or password'
        }, status=401)


@require_POST
def logout_ajax(request):
    logout(request)
    return JsonResponse({
        'status': 'success',
        'message': 'Logout successful!'
    }, status=200)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Cek apakah user adalah pemilik produk
    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    product.name = strip_tags(request.POST.get("name"))
    product.description = strip_tags(request.POST.get("description"))
    product.price = request.POST.get("price")
    product.thumbnail = request.POST.get("thumbnail")
    product.category = request.POST.get("category")
    product.is_featured = request.POST.get("is_featured") == "on"
    
    product.save()
    
    return JsonResponse({
        'status': 'success',
        'message': 'Product updated successfully',
        'product': {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'thumbnail': product.thumbnail,
            'category': product.category,
        }
    }, status=200)


@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Cek apakah user adalah pemilik produk
    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    product.delete()
    
    return JsonResponse({
        'status': 'success',
        'message': 'Product deleted successfully'
    }, status=200)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == "true"
    user = request.user

    new_product = Product(
        name=name,
        description=description,
        price=price,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        user=user,
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=200)

#ubah 1
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')  # balik ke halaman utama toko olahraga

    context = {
        'form': form,
        'product': product,
    }
    return render(request, "main/edit_product.html", context)

#ubah2
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)

    # hanya pemilik produk yang boleh hapus
    if product.user == request.user:
        product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, "main/register.html", context)


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, "main/login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# views.py
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:  # kalau filter != "all", misal filter=user
        products = Product.objects.filter(user=request.user)

    context = {
        'store_name': 'GoalHub',
        'npm': '2406437615',
        'name': request.user.username,
        'class': 'PBP F',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main/main.html", context)


# Data delivery
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

#baru
def show_json(request):
    products = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'description': product.description,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user.id if product.user else None,
        }
        for product in products
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

#baru
def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'description': product.description,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else "Anonymous",
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


@login_required(login_url='/login')
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()
    return render(request, "main/add_product.html", {"form": form})


# Detail
@login_required(login_url='/login')

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    product.product_views += 1
    product.save(update_fields=["product_views"])

    
    return render(request, "main/product_detail.html", {"product": product})
