from django.urls import path
from src import views

urlpatterns = [
    path('jp/', views.home_en, name="home_en"),
    path('en/', views.home_jp, name="home_jp"),
    path('info/', views.info, name="info"),
    path('mtcam/', views.mtcam, name="mtcam"),
    path('powderalert/', views.powderalert, name="powderalert"),
    path('matching/', views.matching, name="matching"),
    path('niseko_en/', views.niseko_en, name="niseko_en"),
    path('niseko_jp/', views.niseko_jp, name="niseko_jp"),
]