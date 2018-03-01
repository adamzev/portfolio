from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
import os
import random

from .forms import WorksheetForm

sys.path.append(os.path.abspath('../grade-it/grade_it'))
from worksheet_gen import generate_worksheet, PDF

def random_hex():
    return str(random.choice("0123456789ABCDEF"))
def get_random_hex(size=10):
    result = "".join([random_hex() for _ in range(size)])
    return result

def worksheet_form(request):
    if request.method == 'POST':
        form = WorksheetForm(request.POST)
        if form.is_valid():
            min_val = form.cleaned_data['min_val']
            max_val = form.cleaned_data['max_val']
            problem_count = form.cleaned_data['problem_count']
            qr = bool(form.cleaned_data.get('qr', False))

            worksheet_specs = {
                "name": "add",
                "qr": qr, 
                "folder" : "static/sheets",
                "qr_type": "answer_key", # or "form_code"
                "random_seed": get_random_hex(),
                "problem_groups": [
                    {
                        "count": problem_count,
                        "group_name": "basicOp",
                        "specs": {
                            "type": "add",
                            "randomize": True,
                            "min_value": min_val,
                            "max_value": max_val

                        }
                    }
                ]
            }

    
            sheet = generate_worksheet(worksheet_specs, display_method=PDF)

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

'''
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
'''