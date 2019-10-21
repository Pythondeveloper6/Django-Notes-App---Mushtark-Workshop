from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Note



def notes(request):
    all_notes = Note.objects.all()
    context = {
     'all_notes' : all_notes ,
    }

    return render(request , 'all_notes.html' , context)


def detail(request , slug):
    note = get_object_or_404(Note , slug=slug)
    print(note)
    context = {
        'one_note' : note ,
    }
    return render(request , 'note_detail.html' , context)
