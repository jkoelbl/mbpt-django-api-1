from django.conf.urls import url

from api.todo.views import TodoList

urlpatterns = [
    url(r'^', TodoList.as_view())
]