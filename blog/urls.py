
from django.urls import path
from . import  views
urlpatterns = [
    path('', views.HomePageVIew.as_view(), name = 'home'),
    path('about/', views.AboutPageVIew.as_view(), name = 'about'),
    path('contact/', views.ContactPageVIew.as_view(), name = 'contact'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name = 'blogurl'),

]
