from django.urls import path
# urls.pyと同じ階層(.)のviewsからclassをインポート
from .views import IndexView,AboutView

# ユーザーがトップページにアクセスしたらIndexViewを開く
urlpatterns = [
    path('', IndexView.as_view()),
    path('about/',AboutView.as_view()),
]