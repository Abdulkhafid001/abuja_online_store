from store import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('home', views.homepage),
    path('studentsapi/', views.Get_students_List.as_view()),
    path('admin/', admin.site.urls),
]
