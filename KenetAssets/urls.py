from django.urls import path
from . import views

urlpatterns = [
    path('consignment/<int:pk>/details/', views.consignment_details, name='consignment-details'),
    # other URL patterns
]
