from django.db import models



class Photo(models.Model):
    #id는 보통 자동 생성
    #upload_to 이걸 중간에 바꿔도 이전에 저장했던거는 예전거로 알아서 참조함
    image = models.ImageField(upload_to='%Y/%m/%d/orig')#원본 사진 파일
    #그리고 이미지 파일은 꼭 이걸 처리해주는 pillow 가 필요하다
    #진짜 꼭 필요함 pip로 설치해보자
    #터미널에서 프로젝트까지 와서 설치를해주는건 기본!
    #그리고 이미지 필드는 기본적으로 파일 필드를 상속받음!
    #필터 적용된 사진 파일
    #얘는 기본적으로 MEDIA_ROOT 아래로 들어가게 되어있음
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    #사진 설명
    #blank =True 는 폼에서 봤을때 빈칸 허용한다는 소리임
    #null = True 는 테이블에서 not null 옵션 제거 그러니까 널 허용한다는소리
    content = models.TextField(max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)         #생성일

    #장고는 객체 하나 지울때 이게 실행된다네
    #이걸 해준 이유가 파일업로드한거 객체지우니까 파일은 안지워짐
    #파일까지 지우려고 이거한거임
    def delete(self, *args, **kwargs):

        self.image.delete()
        self.filtered_image.delete()
        #이부분이 객체를 삭제하는 부분임
        #만약 내가 코드짜서 지우려면 여길 지우고 직접 구현하면됨
        #그러니 이 뜻은 모델을 지워라 이거임 데이터베이스 삭제를 말하는 듯
        #그니까 상속받은애의 딜리트를 실행하라 이거
        super(Photo,self).delete(*args,**kwargs)

