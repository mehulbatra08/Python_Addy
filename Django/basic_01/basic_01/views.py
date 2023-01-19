from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(""" <a href = 'capfirst'> capitalise first </a>
                            <a href = 'newlineremover'> new line remover </a>
                            <a href = 'charcount'> charcount </a> """)
def tutorial(request):
    f = open("/Users/mehulbatra/Desktop/Programming/Python Addy/Django/basic_01/basic_01/Tutorial.txt","r")
    # print(f.read())
    return HttpResponse(f.read())

def Youtube(request):
    return HttpResponse(""" <a href = 'https://www.youtube.com/'> Youtube Link </a>
                            <a href = 'https://www.Facebook.com/'> Facebook Link </a>
                            <a href = 'https://www.Linkedin.com/'> Linkedin Link </a> """)
def capfirst(request):
    return HttpResponse("capfirst")
def newlineremover(request):
    return HttpResponse("newlineremove")
def charcount(request):
    return HttpResponse("charcount")

def tempo(request):
    parameters = {'name':'mehul','location':'mars'}
    return render(request, "jinja.html",parameters)

