from django.urls import path
from knowledge_center_viewer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.edit_article, name='article'),
    path('update_database/', views.update_database, name = 'update_database')
]