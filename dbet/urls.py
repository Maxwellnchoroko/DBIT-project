from . import views
from django.conf.urls import url
from.views import ClientListView,ClientCreateView
from django.conf.urls.static import static,settings


urlpatterns=[
    url('^$',ClientListView.as_view(),name = 'welcome'),
    url(r'^client/new/',ClientCreateView.as_view(), name='client-create'),
    url(r'^client/',views.client, name='client'),
    url(r'^player/',views.player,name='player'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)