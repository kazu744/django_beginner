from django.urls import path
from blog.views import hello_world

urlpatterns = [
    # 引数にURL('～:8000/'以降のURLを指定)、関数、参照用の名前を入れる
    path("", hello_world, name="hello_world"),
]