from django.shortcuts import render
from django.http import HttpResponse
from seedstar_test.models import Contact
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView

# Create your views here.


class ListContactView(ListView):
    model = Contact
    template_name = 'list.html'


class CreateContactView(CreateView):
    model = Contact
    template_name = 'add_contact.html'
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('list')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            contacts = Contact.objects.filter(first_name__icontains= q, last_name__icontains=q)
            return render(request,'list.html',{'contacts':contacts, 'query':q})
        message = 'Nothing to search for'
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts':contacts})


def list_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts': contacts})


def index(request):
    return render(request, 'index.html')

