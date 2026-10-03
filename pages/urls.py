from django.urls import path
from .views import HomePageView, HomeDetailView, HomeDeleteView, HomeNewView, HomeEditView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('car/<int:pk>/', HomeDetailView.as_view(), name='home_detail'),
    path('car/new', HomeNewView.as_view(), name='home_new'),
    path('car/<int:pk>/delete', HomeDeleteView.as_view(), name='home_delete'),
    path('car/<int:pk>/edit', HomeEditView.as_view(), name='home_edit'),
]
