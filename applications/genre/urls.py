from django.urls import path
from applications.genre.views import ListCreateView, DeleteUpdateRetrieveView


urlpatterns = [
    path('', ListCreateView.as_view()),
    path('<int:pk>/', DeleteUpdateRetrieveView.as_view())
]