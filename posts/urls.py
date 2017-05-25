from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'posts'

urlpatterns = [
    #url(r'^$', views.home, name="home"),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_details, name="post_detail"),
    url(r'^create/', views.create, name="create")
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)