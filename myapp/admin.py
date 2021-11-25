from django.contrib import admin
# モデルをインポートする
from . import models

#管理画面に自分の作ったモデルを登録する、ユーザーとグループはデフォルトで存在する

# カテゴリの登録
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Tag)
class tagAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
  pass