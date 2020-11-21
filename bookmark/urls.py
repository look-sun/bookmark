from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/???
    path('', BookmarkListView.as_view(), name='list'), # as_view()가 class 형 뷰를 함수형 뷰로 바꾸어 준다
    path('add/', BookmarkCreateView.as_view(), name='add'), # name=''은 나중에 템플릿에서 주소를 불러올 때 사용하는 이름이다.
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'), # <int:pk> 는 게시판에 게시글의 번호를 할당해 주는 것이다. pk = primary key
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]

