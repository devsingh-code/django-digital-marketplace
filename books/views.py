from django.shortcuts import render, get_object_or_404
from .models import Book, Chapter,Exercise
from django.http import  Http404
# Create your views here.

def book_list(request):
    '''display list of the books'''
    queryset = Book.objects.all()
    context = {
        'queryset': queryset
    }

    return render (request, 'book_list.html',context)


def book_detail(request, slug):
    '''display list of chapters in book and other info regarding book'''
    book = get_object_or_404(Book, slug = slug)
    context ={
        'book': book
    }
    return render(request, 'book_detail.html', context)


def chapter_detail(request, book_slug, chapter_number):
    '''display the list of exercies in the chapter'''
    chapter_qs = Chapter.objects \
        .filter(book__slug=book_slug) \
        .filter(chapter_number=chapter_number)

    if chapter_qs.exists():
        context = {
            'chapter': chapter_qs[0]
        }
        return render(request,"chapter_detail.html",context)
    return Http404


def exercise_detail(request, book_slug, chapter_number, exercise_number):
    exercise_qs = Exercise.objects \
        .filter(chapter__book__slug=book_slug) \
        .filter(chapter__chapter_number=chapter_number) \
        .filter(exercise_number=exercise_number)

    if exercise_qs.exists():
        context = {
            'exercise': exercise_qs[0]
        }
        return render(request,"exercise_detail.html",context)
    return Http404
