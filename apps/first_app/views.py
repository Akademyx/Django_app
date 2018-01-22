from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
  response= "placeholder to display a new form to create a new blog"
  return HttpResponse(response)

def create(request):
  return redirect('/')

def show(request, number):
  print number
  return HttpResponse("This number is {}".format(number))

def edit(request, number):
  response = "placeholder to make an edit of {}".format(number)
  return HttpResponse(response)

def destroy(request, number):
  return redirect('/')
