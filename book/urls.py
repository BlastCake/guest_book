from django.urls import path
from .views import *


urlpatterns = [
    path('', notes_list, name='notes_list_url'),
    path('note/create', NoteCreate.as_view(), name='note_create_url'),
    path('tags', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),

]