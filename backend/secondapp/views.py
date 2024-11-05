from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request , months):
    if months == 'jan':
        return HttpResponse('<h1>hello world</h1>')
    elif months == 'dec':
        return HttpResponse('<h1>Winter Vacations</h1>')
    else :
        return HttpResponse('<h1>URL not found</h1>')


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

