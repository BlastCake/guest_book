from django.shortcuts import render, redirect
from .models import Note
from django.views.generic import View
from .utils import ObjectCreateMixin
from .forms import *

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'book/index.html', context={'notes':notes})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'book/list_tags.html', context={'tags':tags})


class NoteCreate(ObjectCreateMixin, View):
    model_form = NoteForm
    template = 'book/note_create.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'book/tag_create.html'