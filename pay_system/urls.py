from django.urls import path
from . import views

urlpatterns = [
        path('', views.ItemList.as_view()),
        path('item/<int:id>', views.Product.as_view()),
        path('buy/<int:id>', views.BuyProduct.as_view()),
]
