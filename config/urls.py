"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    # config.urls => 1차 url을 설정한것
    # 2차는 앱 안에다가 새 파일을 설정 (bookmark 폴더에 url.py 파일 생성)
    # 1차 -> 2차 -> 3차
    # http://127.0.0.1/bookmark/?
    # ex) http://127.0.0.1/중앙창구/외과
    path('admin/', admin.site.urls),
    path('bookmark/',include('bookmark.urls')),
    path('', include('testapp.urls')),
]
