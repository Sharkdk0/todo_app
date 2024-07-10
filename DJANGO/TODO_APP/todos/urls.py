from django.urls import path
from .views import home, add_todo, show_update, update_todo, delete_todo

urlpatterns = [
    path('home/', home, name="home"),
    path('add-todo/', add_todo, name="add_todo"),
    path('show_update/<int:todo_id>/', show_update, name="show_update"),
    path('update_todo/<int:todo_id>/', update_todo, name="update_todo"),
    path('delete_todo/<int:todo_id>/', delete_todo, name="delete_todo"),
]
