from django.db import models

# カテゴリクラス、最初大文字のクラス名をつける。（modelsのModelを継承して定義する）:
class Category(models.Model):
  # 作るカテゴリの設定
  name = models.CharField(
    max_length=225,
    blank = False,
    null = False,
    unique=True
  )
  # カテゴリ自信の名前を表すpythonの文法
  def __str__(self):
    return self.name

# タグクラス
class Tag(models.Model):
  name = models.CharField(
    max_length=225,
    blank = False,
    null = False,
    unique=True
  )

  def __str__(self):
    return self.name

# 投稿に関するクラス
class Post(models.Model):
# 投稿時
  created = models.DateTimeField(
    auto_now_add = True,
    editable= False,
    blank = False,
    null = False
  )
# 更新時
  updated = models.DateTimeField(
    auto_now = True,
    editable = False,
    blank = False,
    null = False
  )
# タイトル
  title = models.CharField(
    max_length= 225,
    blank = False,
    null = False
  )
# 本文、TextFieldには長さの制限がない
  text = models.TextField(
    max_length=1000,
    blank = True,
    null = False
  )
# カテゴリと投稿を紐づける,投稿に対してカテゴリは一つなのでreignKeyを使う
  Category = models.ForeignKey(
    # 紐づけるクラス名を記入
    Category,
    # カテゴリが削除された時は投稿を削除する
    on_delete = models.CASCADE
  )
# タグと投稿を紐づける、一対多なのでManyToManyFieldを使う
  tags = models.ManyToManyField(
    Tag,
    blank = True
  )

  def __str__(self):
    return self.title




