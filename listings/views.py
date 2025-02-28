from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product,Review
from . forms import ReviewForm
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    requested_category = None
    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)

    return render(
        request,
        'product/list.html',
        {
            'categories': categories,
            'requested_category': requested_category,
            'products': products,
        }
    )
def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    
    
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        
        if review_form.is_valid():
            cf = review_form.cleaned_data
            author_name = "Anonymous"
            if request.user.is_authenticated and request.user.first_name:
                author_name = request.user.first_name
            
            Review.objects.create(
                product=product, 
                author=author_name, 
                rating=cf['rating'], 
                text=cf['text']
            )
            return redirect('listings:product_detail', category_slug=category_slug, product_slug=product_slug)
    else:
        review_form = ReviewForm()
        cart_product_form = CartAddProductForm()

    return render(request, 'product/detail.html', {
        'product': product,
        'review_form': review_form,
        'cart_product_form': cart_product_form,
        'related_products': related_products
    })