from django.shortcuts import render,redirect
# from django.urls import 
from .forms import myForm,picForm
from .models import myRecords,userPics,images
# Create your views here.


def home(request):
    form=myForm()
    picform=picForm()
    context = {'form':form,'picForm':picForm}
    return render(request,'home.html',context)


def allRecords(request):
    records=myRecords.objects.all()
    context = {'records':records}
    return render(request, 'records.html',context)

def insertRecord(request):
    if request.method == "POST":
        form=myForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect("home")

def deleteRecord(request,id):
    record=myRecords.objects.get(id=id)
    record.delete()
    return redirect("allRecords")

def editRecord(request,id):
    record=myRecords.objects.get(id=id)
    if request.method == "POST":
        form=myForm(request.POST, instance=record)
        form.save()
        return redirect("allRecords")
    
    
    form=myForm(instance=record)
    context= {"form":form}
    return render(request, 'edit.html',context)


def uploadImage(request):
    if request.method=='POST':
        user_id = request.POST.get("user_id")
        user = myRecords.objects.get(id=user_id)
        image = request.FILES['user_image']
        data=userPics(user,image)
        data.save()
        return redirect("allRecords")

# def uploadImage(request):
#    return render(request,'uploadImage.html')

def gallary(request):
    if request.method=="POST":
        img=images()
        img.image=request.FILES['pic']
        img.save()
        return redirect("gallary")
    imgs = images.objects.all()
    return render(request,'gallary.html',{'images':imgs})