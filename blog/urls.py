from django.urls import path
from .views import HomePageView, ListView, DetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts/', ListView.as_view(), name='lists'),
    # path('post_details/<int:pk>', DetailView().as_view(), name='details')
]
