from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def TellHello(requests):
    html = "<html>" \
           "<title> practice 1 </title>" \
           "<h1> It's my first django application. </h1></html>"
    return HttpResponse(html)