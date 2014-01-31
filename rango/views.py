from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.
def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', {'':""}, context )

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Ajay Kumar"}
    return render_to_response('rango/index.html', context_dict, context)

