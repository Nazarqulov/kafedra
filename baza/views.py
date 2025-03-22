from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from urllib import request

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm,ProfileForm
from .models import Muallim, News, Loyihalar, Tadbirlar, Talaba, Izohlar, Registr, Salohiyat, Tugarak
from django.contrib.auth import authenticate,login,logout

def index(request):
    tugarak=Tugarak.objects.all()
    talaba=Talaba.objects.all()
    context = {'tugarak':tugarak,'talaba':talaba}

    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "GET":


        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Izohlar.objects.create(**data)
            return redirect('index')
    context = {'form':form}
    return render(request, 'contact.html',context)
def blog(request):
    return render(request, 'blog.html')
def blog_single(request):
    return render(request,'blog-single.html')
def course_grid2(request):
    return render(request,'course-grid-2.html')
def course_grid3(request):
    return render(request,'course-grid-3.html')
def course_grid4(request):
    return render(request,'course-grid-4.html')
def teachers(request):
    domla=Muallim.objects.all()
    context = {'domla':domla}

    return render(request,'trainers.html',context)
def pricing(request):
    return render(request,'pricing.html')
def registration(request):
    if request.method == "GET":
        form = Registr()
    else:
        form = Registr(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Registr.objects.create(**data)
            return redirect('index')
        context = {'form':form}
        return render(request,'registr.html',context)
def Profil(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
           # data = form.cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
           # user = authenticate(username=data['username'], password=data['password'])
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Profil faol emas')
        else:
            return HttpResponse("Login yoki parol xato \n qaytadan urinib ko'ring")
    else:
        form = ProfileForm()
        return render(request,'Login.html',{'form':form})

def courses(request):
    return render(request,'courses.html')
def events(request):

    return render(request,'events.html')

# Create your views here.
