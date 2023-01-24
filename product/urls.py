from django.urls import path
from .views import ( 
    product_list_view,
    product_detail_view,
)

urlpatterns = [
    path('', product_list_view,),
    path('<int:id>/', product_detail_view,),
]

