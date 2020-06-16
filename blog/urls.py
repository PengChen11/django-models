from django.urls import path
from .views import HomePageView, PostDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailsView.as_view(), name='details'),

]
