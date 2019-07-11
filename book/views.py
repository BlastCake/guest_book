from django.shortcuts import render, redirect
from .models import Note
from django.views.generic import View
from .forms import NoteForm


# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'book/index.html', context={'notes':notes})



class NoteCreate(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'book/note_create.html', context={'form':form})

    def post(self, request):
        bound_form = NoteForm(request.POST)

        if bound_form.is_valid():
            note = bound_form.save()
            return redirect(notes_list)

        return render(request, 'book/note_create.html', context={'form': bound_form})

