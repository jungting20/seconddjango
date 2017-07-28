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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
# django.contrib.auth 안에 인증관련 패키지들을 담아둠
from django.contrib.auth import views as auth_views

from photos.views import hello, detail, create, signup


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    url(r'^photos/upload/$', create, name='create'),
        #패턴을 묶는 클라스
        #ctrl shift i 누르면 이동함 컨트롤 클릭하는 번거로움
    url(r'^photos/(?P<pk>\d+)/$', detail, name='detail'),
        # url(r'^photos/(?P<pk>\d+)/$', detail, name='detail',kwargs={'hidden':True}),
        #이런식으로 kwargs에 인자값으로 임의의 값을 넘길 수있음 저걸 받아서 뭐 이것저것
        #할수있지
        #받을때는 인자로 받으면 된다
        #def aa(hidden = False)뭐 이런식으로 ㅋ

        #내장함수 사용 이게 가장 안정적
        #이렇게하면 login내장함수가 form 이라는 이름으로 아이디 비번을 넘김 login.html로 넘김
        #넘기는 폼은 액션값 유알엘에 지정한유알엘 따라감
        #인증 순서
        #양식을 보내면 authenticate()함수가 settings의 BACKENDS 항목에 등록된 인증
        #체계기반 클래스를 하나씩 가져와서 authenticate()메서드를 호출하여 인증을 시도함

    url(r'^accounts/login/',auth_views.login,name='login',kwargs={
            'template_name':'login.html'
    }),
    url(r'^aaa/login/',auth_views.login,name='login2',kwargs={
            'template_name':'login2.html'
    }),
    url(r'^accounts/logout/',auth_views.logout,name='logout',kwargs={
            'next_page':settings.LOGIN_URL
            #여기서 알아야 할 부분은
            #로그인여부를 검사하고 로그인하지않으면 로그인 URL로 사용자를 이동시킴
            #이 URL을 저기서 가져온다 기본값은 /accounts/login/임
            #다른걸 쓰고싶으면 저 항목을 다른걸로 지정하면됨
        }),
    url(r'^users/',include('profiles.urls')),
    url(r'^join/$',signup)
    ]
        #from django.conf.urls.static import static upload_files의 주소를
    #저 document_root의 값으로 매핑 하겠다는 소리야
    #그래서 화면에는 upload_files라고 나오는데 사실은 이게 내가 MEDIA_ROOT에 설정해둔
    #값으로 되는거지 이 설명을 안써줬네
    #궁금하면 컨트롤 클릭해서 들어가보면 자세히 알려준다
    #url(r'^이렇게하고 리턴값 자체가 그 유알엘이야 들어가봐 궁금하면
    #아마 static 메서드가 정적파일을 관리해주는거 같다
    #이게 매핑 값임 매핑이 여기서 되는거임 세팅에서는 그냥 아무것도안됨 매핑은 꼭여기서
urlpatterns +=static('upload_files',document_root=settings.MEDIA_ROOT)
    #가장 중요한건 static함수는 셋팅에서 DEBUG=True 인경우에만 동작한다는 거다
    #static 파일은 이런거 안해줘도 된다 그냥 알아서 해줌

    #바디태그가있어야 동작함디버그 툴바
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]