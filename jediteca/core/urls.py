from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^', views.livros_list),
    url(r'^login/',views.tela_login),

]
