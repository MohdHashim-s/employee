from django.shortcuts import render, redirect
from . models import Employee
from . forms import EmpForm
# Create your views here.
def index(request):
    movie=Employee.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)


def detail(request, emp_id):
    movie = Employee.objects.get(id=emp_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        email = request.POST.get('email',)
        address = request.POST.get('address',)
        img = request.FILES['img']
        desig=request.POST.get('desig')
        movie=Employee(name=name,email=email,address=address,img=img,desig=desig)
        movie.save()


    return render(request,'add.html')


def update(request,id):
    movie=Employee.objects.get(id=id)
    form=EmpForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Employee.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
