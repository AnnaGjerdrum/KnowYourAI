from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.

# add new page (view)
# also add in urls

# with database objects::
# def URL(request):
#    variable = DATABASE.objects.all()
#    return render(request, 'URL.html', { 'nameOfVariable': variable })

# without database objects
# def URL(request):
#    return render(request, 'URL.html')

class index_view(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

#What is AI?

def input(request):
    return render(request, 'input.html')

def data(request):
    return render(request, 'data.html')

def learning(request):
    return render(request, 'learning.html')

def mistakes(request):
    return render(request, 'mistakes.html')

def output(request):
    return render(request, 'output.html')

#Usage

def where(request):
    return render(request, 'where.html')

def why(request):
    return render(request, 'why.html')

def jobs(request):
    return render(request, 'jobs.html')

def jobs2(request):
    return render(request, 'jobs2.html')

def danger(request):
    return render(request, 'danger.html')

# Ethics

def ethics(request):
    return render(request, 'ethics.html')

def privacy(request):
    return render(request, 'privacy.html')

def influence(request):
    return render(request, 'influence.html')

def weapons(request):
    return render(request, 'weapons.html')

def account(request):
    return render(request, 'account.html')

# Teach your AI

def game(request):
    return render(request, 'game.html')

def object(request):
    return render(request, 'object.html')

def language(request):
    return render(request, 'language.html')

# Algorithms

def OAlgo(request):
    return render(request, 'OAlgo.html')
