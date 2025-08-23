from products.models import ProductForm,Product
from django.shortcuts import render, get_object_or_404, redirect

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()### It save the data into database
            return redirect('product_list')
  
    return render(request, 'product_create.html')

def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_update(request, pk):
    product= get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form})

def product_delete(request, pk):
    product= get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        Product.delete()
        return redirect('product_create_list')
    return render(request, 'product_delete.html', {'product': product})


def home(request):
    # You can customize this query to fetch only featured products
    products = Product.objects.all()[:8]  # Show latest 8 products
    
    return render(request, 'home.html', {'products': products})
