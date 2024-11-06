from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def index(request , months):
#     if months == 'jan':
#         return HttpResponse(request.method)
#     elif months == 'dec':
#         return HttpResponse('<h1>Winter Vacations</h1>')
#     else :
#         return HttpResponse('<h1>URL not found</h1>')

# def index(request , months):
#     if request.method == 'GET':
#         return HttpResponse('<h1>hello world {}</h1>'.format(request.method))
#     elif request.method == 'Post':
#         return HttpResponse(f'<h1>Winter Vacations {request.method}</h1>')
#     elif request.method == 'Put':
#         return HttpResponse(f'<h1>Summer Vacations {request.method}</h1>')
#     elif request.method == 'delete':
#         return HttpResponse(f'<h1>Autumn Vacations {request.method}</h1>')
#     else :
#         return HttpResponse('<h1>URL not found</h1>')

# def jan(request):
#     return HttpResponse('<i>Front-End</i>')
# def feb(request):
#     return HttpResponse('<i>Back-End</i>')
# def mar(request):
#     return HttpResponse('<i>React</i>')
# def apr(request):
#     return HttpResponse('<i>DBMS</i>')
# def may(request):
#     return HttpResponse('<i>Python</i>')
# def jun(request):
#     return HttpResponse('<i>Node js</i>')
# def jul(request):
#     return HttpResponse('<i>Flutter & Dart</i>')
# def aug(request):
#     return HttpResponse('<i>Machine Learning</i>')
# def sep(request):
#     return HttpResponse('<i>Git & Github</i>')
# def oct(request):
#     return HttpResponse('<i>DJango</i>')
# def nov(request):
#     return HttpResponse('<i>BootStrap</i>')
# def dec(request):
#     return HttpResponse('<i>Mobile App Development</i>')

class index(View):
    def get(self , request):
        method = request.method
        return HttpResponse(f'response to GET request ,{method}')
    

# class index(View):
#     def get(self , request):
#         return HttpResponse('response to POST request')    