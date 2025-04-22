from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def insert(request):
    if request.method=='POST':
        nm=request.POST['name']
        ag=request.POST['age']
        em=request.POST['email']
        dp=request.POST['dept']
        Student.objects.create(name=nm,age=ag,email=em,dept=dp)
        return redirect('read')
    return render(request,'main.html')

def read(request):
    j=Student.objects.all()
    return render(request,'home.html',{'student':j})

def update(request,u):
    context={
            "all":Student.objects.get(id=u)
        }
    if request.method=="POST":
        nm=request.POST['name']
        ag=request.POST['age']
        em=request.POST['email']
        dp=request.POST['dept']
        t=Student.objects.get(id=u)
        t.name=nm
        t.age=ag
        t.email=em
        t.dept=dp
        t.save()
        return redirect('read')
    return render (request,"main.html",context)

def delete(request,k):
    s=Student.objects.get(id=k)
    s.delete()
    return redirect ("read")




