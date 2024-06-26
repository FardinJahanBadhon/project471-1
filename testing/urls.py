from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('addu/', views.tryf, name='okay'),
    path('see/',views.product_list, name= 'product'),
    path('',views.product_list_shop, name= 'shop_product'),
    path('success/', views.addProduct, name= 'addP'),
    path('seee/', views.trial , name='test'), 
    path('alter/<int:product_id>/', views.edit, name='edit'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('product/<str:product_id>/', views.show_product, name='show_product'),
    path('combo/',views.p, name= 'combo_add'),
    path('add_combo/', views.add_combo, name='add_combo'),
    # path('products/', views.top_product, name='top_product_list'),
    path('combov/', views.see_combo),
    path('combosee/', views.combo_detail, name='combo_detail'),
    path('rating-view/', views.rating_view, name='rating_view'),
    path('skin_product/', views.skin_product, name='skin_product'),
    path('hair_product/', views.hair_product, name='hair_product'),
    path('makeup_product/', views.makeup_product, name='makeup_product'),
    path('others_product/', views.others_product, name='others_product'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)