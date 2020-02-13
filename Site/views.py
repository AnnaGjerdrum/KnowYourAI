from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.

class index_view(TemplateView):
    template_name = 'index.html'

    def get(self, request):
    #    subjects = Subject.objects.all()
    #    books = Book.objects.all()
    #    unis = University.objects.all()
    #    context = {
    #        'subjects': subjects,
    #        'books': books,
    #        'unis': unis,
    #        }
        return render(request, self.template_name) #, context)
