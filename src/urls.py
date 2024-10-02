from django.urls import path
from src import views

urlpatterns = [
    path('', views.home_en, name="home"),
    # path('jp/', views.home_jp, name="home_jp"),
    path('info/', views.info, name="info"),
    path('mtcam/', views.mtcam, name="mtcam"),
    path('powderalert/', views.powderalert, name="powderalert"),
    path('matching/', views.matching, name="matching"),
    path('niseko/en/', views.niseko_en, name="niseko_en"),
    path('niseko/jp/', views.niseko_jp, name="niseko_jp"),
]