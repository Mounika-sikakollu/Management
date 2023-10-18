from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('news',views.news,name='news'),
    path('more',views.more,name='more'),
]