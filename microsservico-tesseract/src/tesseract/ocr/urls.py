from django.urls import path
from . import views
from .views import OcrView

urlpatterns = [
    path('', views.index, name='index'),
    path('ocr/', OcrView.as_view()),
]
