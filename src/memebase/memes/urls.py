from django.urls import path
from .views import meme_list, load_more_memes

app_name = 'memes'

urlpatterns = [
    path('', meme_list, name='meme_list'),
    path('load-more-memes/', load_more_memes, name='load_more_memes'),
]
