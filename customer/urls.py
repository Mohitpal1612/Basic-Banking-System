from django.urls import path
from . import views

urlpatterns = [

    path('', views.customer_details, name='customer'),
    path('customer_by_ac/<id>/',views.customer_bank_detail),
    path('transaction',views.transaction)
]