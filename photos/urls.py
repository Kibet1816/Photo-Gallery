from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^categories/',views.categories,name='categories'),
    url('^travel',views.travel,name='travel'),
    url('^food',views.food,name='food'),
    url('^sport',views.sport,name='sport'),
    url('^animals',views.animals,name='animals'),
    url('^architecture',views.architecture,name='architecture'),
    url('^landscapes',views.landscapes,name='landscapes'),
    url('^search_results',views.search,name='search_results')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
