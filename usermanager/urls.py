from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='usermanager'
urlpatterns = [
    url(r'^register$',views.Register.as_view(), name='register'),
    url(r'^login$',views.Login.as_view(), name='login'),
    url(r'^publish$',views.Publish.as_view(), name='publish'),
    url(r'^signout$',views.SignOut.as_view(), name='signout'),

]
