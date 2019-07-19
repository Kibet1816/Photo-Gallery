from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^categories/',views.categories,name='categories'),
    url('^location/',views.location,name='location'),

]