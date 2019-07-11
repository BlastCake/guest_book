from django.urls import path
from .views import *


urlpatterns = [
    path('', notes_list, name='list_notes'),
    path('create/', NoteCreate.as_view(), name='note_create_url')
]