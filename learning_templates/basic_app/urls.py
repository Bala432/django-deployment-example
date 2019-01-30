from django.urls import re_path
from basic_app import views
from django.conf.urls import url

#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/',views.relative,name='relative'),
    re_path('other/',views.other,name='other'),
]
