from django.contrib.auth import login
from django.urls import path
from django.views.generic import detail

from .views import index,about,contact,blog_single,blog,course_grid2,course_grid3,course_grid4,teachers,pricing,registration,Profil,courses,events


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog-single/', blog_single, name='blog-single'),
    path('teachers/', teachers, name='trainers'),
    path('blog/', blog, name='blog'),
    path('course_grid2/', course_grid2, name='course_grid2'),
    path('course_grid3/', course_grid3, name='course_grid3'),
    path('course_grid4/', course_grid4, name='course_grid4'),
    path('pricing/', pricing, name='pricing'),
    path('registration/', registration, name='registration'),
    path('Profil/', Profil, name='Profil'),
    path('courses/', courses, name='courses'),
    path('events/', events, name='events'),





]