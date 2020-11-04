from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView
from .models import Client,Player
from .forms import ClientForm,PlayerForm
from django.contrib.auth.models import  User

# Create your views here.
def welcome(request):
   context= {
      'clients':Client.objects.all()
   }
   return render(request, 'welcome.html',context)

class ClientListView(ListView):
     model =Client 
     template_name='welcome.html' 
     context_object_name ='clients'
     ordering =['-pub_date']

class ClientCreateView(LoginRequiredMixin,CreateView):
     model =Client 
     fields =['first_name','last_name','email','phone_number','needed_xpertise']


def client(request):
    title = 'CLIENTS'
    if request.method=='POST':
        form = ClientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form =ClientForm()
    return render (request,'client.html',{'form':form,'title':title})

def player(request):
    title = 'PLAYER'
    if request.method=='POST':
        form = PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form=PlayerForm()
    return render(request,'player.html',{'form':form,'title':title})
# def my_students(request):
#     title='STUDENT AVAILLABLE'
#     user = request.user
#     students = Student.objects.all().filter(owner__username=user)
#     return render (request,'students.html',{'title':title,'students':students,'awards':'awards'})

