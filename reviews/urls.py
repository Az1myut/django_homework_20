from django.urls import path
from .views import show_reviews
app_name='reviews'
urlpatterns = [
    path('', show_reviews, name='show_reviews')
]