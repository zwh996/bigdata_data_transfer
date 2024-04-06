"""
URL configuration for data_transfer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from kafka_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/test_kafka_producer", views.kafka_producer_view, name="test_kafka_produce"),
    path("api/test_kafka_consumer", views.kafka_consumer_view, name="test_kafka_produce"),
    path("api/kafka_message_view", views.kafka_message_view, name="test_kafka_produce")

]
