from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CatgoryProduct, Product, Comments, Basket
from .forms import CommentForm, EditCommentForm, DeliveryRegistrationForm

# Create your views here.

HOST = 'http://127.0.0.1:8000/'

def product_categories(request, category_id):
    product_categories = CatgoryProduct.objects.all()
    category = None
    if category_id:
        category = CatgoryProduct.objects.get(id=category_id)
    products_of_category = category.product_set.all()
    context = {'product_categories': product_categories, 
               'category': category, 
               'products_of_category': products_of_category,
               'title_page': category.name}
    return render(request, 'product_categories.html', context)


def info_about_product(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comments.objects.filter(product=product)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.product = product
            new_comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
    context = {'product': product, 
               'form': form, 
               'comments': comments,
               'title_page': product.name}
    return render(request, 'info_about_product.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    if request.method == 'POST':
        form_edit_comment = EditCommentForm(request.POST, instance=comment)
        if form_edit_comment.is_valid():
            comment.comment = form_edit_comment.cleaned_data['comment']
            form_edit_comment.save()
            return redirect(f'{HOST}products/info_about_product/{str(comment.product.id)}')
    else:
        form_edit_comment = EditCommentForm(instance=comment)
    context = {'form_edit_comment': form_edit_comment,
               'title_page': 'Изменить комментарий'}
    return render(request, 'edit_comment.html', context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect(f'{HOST}products/info_about_product/{str(comment.product.id)}')


@login_required
def basket(request):
    basket = Basket.objects.filter(user_for_basket=request.user)
    
    basket_values = list(basket.values('user_for_basket__username', 'user_for_basket__first_name', 'product_for_basket__name', 'quantity'))  # Преобразуем QuerySet в список словарей
    modified_basket_values = []
    for item in basket_values:
        modified_item = {
        'Username': str(item['user_for_basket__username']) + '\n',
        'Имя': str(item['user_for_basket__first_name']) + '\n',
        'Название продукта': str(item['product_for_basket__name']) + '\n',
        'Количество': str(item['quantity']) + '\n',
        }
        modified_basket_values.append(modified_item)
    
    total_price = sum(item.update_total_price() for item in basket)
    if request.method == 'POST':
        form = DeliveryRegistrationForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.basket = basket.first()
            new_order.basket_information = modified_basket_values
            new_order.save()
            return render(request, 'success_order.html', {'new_order_id': new_order.id, 'title_page': 'Заказ оформлен!'})
    else:
        form = DeliveryRegistrationForm()
        
    context = {'basket': basket, 
               'total_price': total_price, 
               'form': form,
               'title_page': 'Корзина'}
    return render(request, 'basket.html', context)



@login_required
def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    add_item, created_item = Basket.objects.get_or_create(user_for_basket=user, product_for_basket=product)
    if not created_item:
        add_item.quantity += 1
        add_item.save()
    return redirect(f'{HOST}products/info_about_product/{str(product.id)}')


@login_required
def delete_from_basket(request, product_id):
    product = Basket.objects.get(id=product_id)
    product.delete()
    
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def increase_quantity(request, product_id):
    product = Basket.objects.get(id=product_id)
    product.increase_quantity()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def decrease_quantity(request, product_id):
    product = Basket.objects.get(id=product_id)
    product.decrease_quantity()
    return redirect(request.META.get('HTTP_REFERER'))


    
    
    


# def info_about_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     comments = Comments.objects.filter(product=product)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.user = request.user
#             new_comment.product = product
#             new_comment.save()
#             return redirect(request.META.get('HTTP_REFERER'))
#     else:
#         form = CommentForm()
#     context = {'product': product, 'form': form, 'comments': comments}
#     return render(request, 'info_about_product.html', context)


# def info_about_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     comments = Comments.objects.filter(product=product)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment_id = form.cleaned_data.get('comment_id')
#             if comment_id:
#                 comment = get_object_or_404(Comments, id=comment_id)
#                 comment.comment = form.cleaned_data['comment']
#                 comment.save()
#             else:
#                 new_comment = form.save(commit=False)
#                 new_comment.user = request.user
#                 new_comment.product = product
#                 new_comment.save()
#                 return redirect(request.META.get('HTTP_REFERER'))
#     else:
#         form = CommentForm()
#     context = {'product': product, 'form': form, 'comments': comments}
#     return render(request, 'info_about_product.html', context)
