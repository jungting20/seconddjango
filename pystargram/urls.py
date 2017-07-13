"""pystargram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from photos.views import hello, detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    #패턴을 묶는 클라스
    #ctrl shift i 누르면 이동함 컨트롤 클릭하는 번거로움
    url(r'^photos/(?P<pk>\d+)/$', detail, name='detail'),
]
#from django.conf.urls.static import static upload_files의 주소를
#저 document_root의 값으로 매핑 하겠다는 소리야
#그래서 화면에는 upload_files라고 나오는데 사실은 이게 내가 MEDIA_ROOT에 설정해둔
#값으로 되는거지 이 설명을 안써줬네
#궁금하면 컨트롤 클릭해서 들어가보면 자세히 알려준다
#url(r'^이렇게하고 리턴값 자체가 그 유알엘이야 들어가봐 궁금하면
urlpatterns +=static('upload_files',document_root=settings.MEDIA_ROOT)
