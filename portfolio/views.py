from django.shortcuts import render
from django.http import HttpResponseRedirect
#from talk.models import Post
#from talk.forms import PostForm


def home(req):

    tmpl_vars = {
        'prob': "2 + 3",
        'result': 5
    }

    return render(req, 'grade-it/index.html', tmpl_vars)


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

