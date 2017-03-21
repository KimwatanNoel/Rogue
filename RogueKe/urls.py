from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'RogueKe'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^fashion/', views.fashion_view, name='fashion'),
    url(r'^technology', views.technology_view, name='technology'),
    url(r'^lifestyle', views.lifestyle_view, name='lifestyle'),
    url(r'^mantalk', views.man_view, name='mantalk'),
    url(r'^trending', views.trend_view, name='trending'),
    url(r'^sports', views.sports_view, name='sports'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

