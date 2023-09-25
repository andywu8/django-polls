from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.urls import reverse

def index(request):
    # return HttpResponse("Hello, world. You're at the index.")
    return render(request,'main/index.html')
    # template = loader.get_template("main/index.html")
    # return HttpResponse(template.render(request))

