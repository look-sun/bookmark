# from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# class형 뷰, function형 뷰
# 미리 만들어 놓은 뷰를 제네릭 뷰 라고 하는데 이는 클래스 형의 뷰이다.
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

# class(클래스) 뷰가 function(함수형) 뷰 보다 사용하기가 더 용이하다. -> 미리 준비되어있기 때문에.
# 하지만 안에있는 내용을 더 깊게 보거나 컨트롤 하려면 함수형 뷰를 사용해야한다.
class BookmarkListView(ListView):   # class => 상속받아 사용한다.
    model = Bookmark    # class 형 뷰는 무조건 이게 들어간다.(CRUD만)

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'site_url']  # fields는 해당 모델에서 어떠한 필드를 수정할지 결정하는 것이다. (all 로 하면 모두 수정)
    success_url = reverse_lazy('list')      # 성공했을때의 뷰 => urls.py 에 있는 name 의 값을 가져오면 됨
    template_name_suffix = '_create'    # django 에서는 기본적으로 update view and create view 에는 _form 이 붙게 되어있는데(왜냐 입력받으면 그걸 수정해야하니까) 그걸 _create 로 바꾸었다.

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'site_url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
