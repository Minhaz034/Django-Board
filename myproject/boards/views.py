from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all()


    #response_html = response_html.join(board_description)
    return render(request, 'home.html',{'boards':boards})
