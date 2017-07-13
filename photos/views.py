import sys

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from photos.models import Photo


def hello(request):
    return HttpResponse('안녕하세요!')


def detail(reuqest,pk):
    photo = get_object_or_404(Photo,pk=pk)
    msg = ('{} 번 사진 보여줄게요'.format(pk),
           #헷갈리게 만들어놨음 아마 버전업되면서 바뀐듯
           #그냥 저렇게 image.url이나 image나 같은거같지만
           #.url로 접근해줘야 진정한str로 그냥접근은 그냥 객체로 접근함!
           '<p>주소는 {url}</p>'.format(url=photo.image.url),
           '<p><img src="{url}"/></p>'.format(url=photo.image.url)
           )

    return HttpResponse(msg)