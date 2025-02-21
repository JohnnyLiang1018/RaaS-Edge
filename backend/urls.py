"""robotrainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from backend.views import InputFormCreateView
from backend.views import VectorFormCreateView

urlpatterns = [
    path('', views.home, name="home"),
    path('customer_data/', InputFormCreateView.as_view(), name="customer_data"),
    path('customer_data/save_data', views.save_robot_actions, name="save_robot_actions"),
    path('vector_data/', VectorFormCreateView.as_view(), name="vector_data"),
    path('vector_data/save_vector_data', views.save_vector_data, name="save_vector_data")

    # path('/', include('api.urls'))
]
