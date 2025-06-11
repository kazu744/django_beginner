from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    # 引数にURL('http://127.0.0.1:8000/'以降のURLを指定)、関数、参照用の名前を入れる
    path("", post_list, name="post_list"),
    path("post/<int:post_id>", post_detail, name="post_detail"),
]