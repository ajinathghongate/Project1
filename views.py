from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Note
from .forms import NoteForm


def note_list(request):
    """Display all notes"""
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    """Display a single note"""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    """Create a new note"""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Create Note'})


def note_edit(request, pk):
    """Edit an existing note"""
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Edit Note', 'note': note})


def note_delete(request, pk):
    """Delete a note"""
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
