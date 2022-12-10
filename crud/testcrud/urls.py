from django.contrib import admin
from django.urls import path
from testcrud import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
]
