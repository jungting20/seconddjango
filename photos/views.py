from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from photos.forms import PhotoForm, UserForm
from photos.models import Photo


def hello(request):
    return HttpResponse('안녕하세요!')


def detail(request,pk,next=1):
    next = request.GET.get('next')
    photo = get_object_or_404(Photo,pk=pk)
    msg = ('{} 번 사진 보여줄게요'.format(pk),
           #그냥 저렇게 image.url이나 image나 같은거같지만
           #.url로 접근해줘야 진정한str로 그냥접근은 그냥 객체로 접근함!
           #.url은 디비에서 긁어오는듯
           '<p>주소는 {url}</p>'.format(url=photo.image.url),
           '<p><img src="{url}"/></p>'.format(url=photo.image.url),
           '<p>next는{}</p>'.format(next),
           )

    return HttpResponse(msg)

#@login_required(login_url='/accounts/login/')이렇게 해도되는듯
@login_required
def create(request):
    #이부분은 이렇게 구현해 줘야하지만
    #login_required 데커레이터를 이용하면 이게 됨 그냥
    #settings.LOGIN_URL 이부분이 중요
    # if not request.user.is_authenticated():
    #     return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        form = PhotoForm()
        # PhotoForm(instance=객체)
        #이런식으로 쳐 넣으면 그냥 들어가서 그거 그대로 뽑아서 보여주기 가능
        #수정할때 필요함
    elif request.method == "POST":
        #무조건 파일하고 분리해줘야함
        form = PhotoForm(request.POST,request.FILES)
        #이방법과
        #form.is_bound =True
        #form.data = request.POST
        #form.files = request.FILES

        if form.is_valid():
            #is_valid 로 한번 걸러진 데이터는 clened_data['key']로 접근해줘야함!!
            obj = form.save(commit=False)
            #로그인을 하지 않으면 여기서 에러가난다
            #user 값이 없으니까
            obj.user = request.user
            #세션에서 불러오는듯
            obj = form.save()
            #리얼 이거 스킬이네 리다이렉트에 모델객체가 넘어갈 경우
            #그 객체의 get_absolute_url()메서드를 호출한다!
            #그니까 이 객체의 원래 클래스에 정의해주는거임!
            #모델.py에있는거지
            #이거 만들어 줘야함
            return redirect(obj)

    return render(request,'edit.html',context={
        'form':form
    })

def signup(request):
    form = UserForm()

    return render(request,'addjoin.html',context={
        'form':form
    })

