from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('feedback',views.feedback,name='feedback'),
    path('services',views.services,name='services'),
    path('update',views.update,name='update'),
]