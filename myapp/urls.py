from django.urls import path
# urls.pyと同じ階層(.)のviewsからIndexViewをインポート
from .views import IndexView

# ユーザーがトップページにアクセスしたらIndexViewを開く
urlpatterns = [
    path('', IndexView.as_view()),
]