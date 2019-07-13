from django.shortcuts import render, redirect
from .models import Note
from django.views.generic import View
from .utils import ObjectCreateMixin
from .forms import NoteForm

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'book/index.html', context={'notes':notes})



class NoteCreate(ObjectCreateMixin, View):
    model_form = NoteForm
    template = 'book/note_create.html'