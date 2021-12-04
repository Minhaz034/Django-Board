from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


# Create your views here.
def home(request):
    boards = Board.objects.all()
    #response_html = response_html.join(board_description)
    return render(request, 'boards/home.html',{'boards':boards})

def about(request):

    data = {'posts':posts}
    return render(request, 'boards/about.html',data)


