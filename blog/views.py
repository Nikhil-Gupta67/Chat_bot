from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the blog index.")

def specific(request):
    return HttpResponse("This is a specific view in the blog app.")

def article_detail(request, article_id):
    return HttpResponse(f"You're looking at article {article_id}.")

def index(request):
    return render(request, 'index.html')

def get_response(request):
    return HttpResponse("This is the response from the get_response view.")