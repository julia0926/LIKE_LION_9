"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.main,name='main'), #제일 첫 화면 메인
    path('detail/<str:id>', blog.views.detail, name="detail"), # 디테일페이지 경로(id 값에 따라서 상세페이지가 다르게 보임 )
    path('write/create/', blog.views.create, name="create"), #글 작성페이지 경로 (forms를 사용하여 함수를 따로 작성하여 create되게)
    path('edit/<str:id>',blog.views.edit,name="edit"), #수정페이지 경로 (디테일과 마찬가지로 글 id값에 따라 다르게 보여아함)
    path('delete/<str:id>',blog.views.delete,name="delete"), #삭제페이지 (수정페이지와 동일)
    path('hashtag/',blog.views.hashtagform,name="hashtag"), #해쉬태그 추가하는 페이지
    path('search/<int:hashtag_id>',blog.views.search,name="search"), #해쉬태그 검색 페이지
    path('account/',include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
