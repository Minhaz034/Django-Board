from django.db.backends.utils import CursorDebugWrapper
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.db import connection


def sql():
    cursor = connection.cursor()
    cursor.execute("select top 100 * from VIEW_CREDITANALYSISFINAL")
    row = cursor.fetchall()
    return row


def group_wise_customers():
    cursor = connection.cursor()
    cursor.execute("""
        select GradingDetails,COUNT(CustomerCode) as Ncustomers
        from VIEW_CREDITANALYSISFINAL
        group by GradingDetails
    """)
    data = cursor.fetchall()
    return data


# Create your views here.
def home(request):
    boards = Board.objects.all()
    #response_html = response_html.join(board_description)
    return render(request, 'boards/home.html',{'boards':boards})

def about(request):
    #data = {'posts':posts}
    data = sql()
    data_dict = {'customers':data}
    return render(request, 'boards/about.html',data_dict)

def groups(request):
    data2 = group_wise_customers()
    data_dict2 = {'groups':data2}
    return render(request,'boards/about.html' ,data_dict2)

def dashboard_home(request):
    data2 = group_wise_customers()
    data_dict2 = {'groups':data2}
    return render(request,'dashboard/dashboard.html' ,data_dict2)


