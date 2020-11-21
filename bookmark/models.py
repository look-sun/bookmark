from django.db import models
from django.urls import reverse

# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 우리가 데이터를 객체화하여 다루겠다.
# 모델 = 데이블 (데이터베이스)
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드) = 레코드의 컬럼 데이터 값
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.URLField('Site URL')  #URLField로 지정하면 자동으로 하이퍼링크가 생성된다.
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 종류
    # 2. 제약 사항 (몇글자까지)
    # 3. Form의 종류
    # 4. Form에서 제약사항

    # 어떤 인스턴스를 프린팅 했을때 나오는 내용은 str method를 사용하면 바뀌기도 한다
    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.site_url       # return한 내용이 출력이 된다.

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])    # str() 로 self.id 를 감싸도 좋다.

# 모델을 만들었다 => 데이터베이스에서 어떤 데이트들을 어떠한 형태로 넣을지 결정!
# 마이그레이션(마이그레이트, migrate) => 데이터베이스에서 모델의 내용을 반영(테이블 생성)
# makemigrations => 모델의 변경사항을 추적해서 기록
# 모델을 수정했다 => 마이그레이션을 해야한다!
