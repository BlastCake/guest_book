from django.shortcuts import render
from .models import Note

# Create your views here.
def notes_list(request):
    notes = Note.objects.get.all()
    return render(request, 'book/index.html', context={'notes':notes})
