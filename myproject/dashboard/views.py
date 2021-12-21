from django.db.backends.utils import CursorDebugWrapper
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def group_wise_customers():
    cursor = connection.cursor()
    cursor.execute("""
        select GradingDetails,COUNT(CustomerCode) as Ncustomers
        from VIEW_CREDITANALYSISFINAL
        group by GradingDetails
    """)
    data = cursor.fetchall()
    return data


def dashboard_home(request):
    data2 = group_wise_customers()
    data_dict2 = {'groups':data2}
    return render(request,'dashboard/dashboard.html' ,data_dict2)
