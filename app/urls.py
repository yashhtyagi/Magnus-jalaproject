from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('tabs/', views.tabs, name='tabs'),
    path('menu/', views.menu, name='menu'),
    path('collapsiblecontent/', views.collapsiblecontent, name='collapsiblecontent'),
    path('images/', views.images, name='images'),
    path('slider/', views.slider, name='slider'),
    path('tooltip/', views.tooltip, name='tooltip'),
    path('popups/', views.popups, name='popups'),
    path('links/', views.links, name='links'),
    path('cssproperties/', views.cssproperties, name='cssproperties'),
    path('iframe/', views.iframe, name='iframe'),
    path('404/', views.page_404, name='404'),
    path('500/', views.page_500, name='500'),
    path('301/', views.page_301, name='301'),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)