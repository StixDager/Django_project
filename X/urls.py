from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Добавьте этот импорт

# Простая view-функция для главной страницы
def home_view(request):
    return HttpResponse("Привет SkillFactory. Добро пожаловать на главную страницу!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', home_view, name='home'),  # Добавьте эту строку
]