from django.conf.urls import url

from profiles import views
urlpatterns = [
    #오타나면안됨!
    url(r'^(?P<username>[\w@+-]+)/$',views.profile,name='profile')

]