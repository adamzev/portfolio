from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
import os

from .forms import WorksheetForm

sys.path.append(os.path.abspath('../grade-it'))
from worksheet_gen import WorksheetGen
#from talk.models import Post
#from talk.forms import PostForm


def worksheet_form(request):
    if request.method == 'POST':
        form = WorksheetForm(request.POST)

        if form.is_valid():
            min_val = form.cleaned_data['min_val']
            max_val = form.cleaned_data['max_val']
            problem_count = form.cleaned_data['problem_count']
            qr = bool(form.cleaned_data.get('qr', False))

            specs = {
                "problem_type": "add",
                "problem_count": problem_count,
                "min_val" : min_val,
                "max_val" : max_val,
                "qr" : qr,
                "folder" : "static/sheets"
            }
            my_gen = WorksheetGen("add", "add", specs)

            sheet = my_gen.create_sheet()
            sheet = sheet.replace("portfolio", "")
            view_data = {
                'result': sheet
            }

            return render(request, 'grade-it/worksheet.html', view_data)

    else:
        form = WorksheetForm()
    
    view_data = {
        'form': form,
    }

    return render(request, 'worksheet_form.html', view_data)


def addTwo(request):
    view_data = {
        'result': 'not yet'
    }
    min_val = request.POST['min_val']
    max_val = request.POST['max_val']
    problem_count = request.POST['problem_count']
    qr = request.POST.get('QR', False)


    if request.method == 'POST':
        view_data['result'] = request.POST['min_val']
    
    return render(request, 'grade-it/worksheet.html', view_data)

def createWorksheet(request):
    # http://127.0.0.1:8000/static/sheets/add_2018-01-23_17-40-47.pdf

    if request.method == 'POST':
        min_val = int(request.POST['min_val'])
        max_val = int(request.POST['max_val'])
        problem_count = int(request.POST['problem_count'])
        qr = bool(request.POST.get('qr', False))

    specs = {
        "problem_type": "add",
        "problem_count": problem_count,
        "min_val" : min_val,
        "max_val" : max_val,
        "qr" : qr,
        "folder" : "static/sheets"
    }
    my_gen = WorksheetGen("add", "add", specs)

    sheet = my_gen.create_sheet()
    sheet = sheet.replace("portfolio", "")
    view_data = {
        'result': sheet
    }

    return render(request, 'grade-it/worksheet.html', view_data)
