from django.urls import path
from .views import review_page

urlpatterns = [
    path('review/', review_page, name='review_page'),
]
