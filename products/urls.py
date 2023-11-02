from django.urls import path
from .views import product_categories, info_about_product, edit_comment, delete_comment, basket, add_to_basket, delete_from_basket, increase_quantity, decrease_quantity

app_name = 'products'

urlpatterns = [
    path('product_categories/<int:category_id>', product_categories, name='product_categories'),
    path('info_about_product/<int:product_id>', info_about_product, name='info_about_product'),
    path('edit_comment/<int:comment_id>', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
    path('basket', basket, name='basket'),
    path('add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('delete_from_basket/<int:product_id>/', delete_from_basket, name='delete_from_basket'),
    path('increase_quantity/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
]



