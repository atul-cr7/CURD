from django.shortcuts import render,HttpResponseRedirect
from .forms import login
from .models import Data

# Create your views here.
def reg(request):
    if(request.method=='POST'):
        fm=login(request.POST)
        if(fm.is_valid()):
            na=fm.cleaned_data['Name']
            em = fm.cleaned_data['Email']
            pa = fm.cleaned_data['Password']
            gm = Data(Name=na, Email=em,Password=pa)
            gm.save()
            fm=login()


    else:
        fm=login()
    stu=Data.objects.all()
    return render(request,'student/enroll.html',{'form':fm,'st':stu})


def delete(request,my_id):
    if(request.method=='POST'):
        gm=Data.objects.get(pk=my_id)
        gm.delete()
        return HttpResponseRedirect('/')

def update(request,my_id):
    if(request.method=='POST'):
        gm=Data.objects.get(pk=my_id)
        fm=login(request.POST ,instance=gm)
        if(fm.is_valid()):
            fm.save()
    else:
        gm=Data.objects.get(pk=my_id)
        fm=login(instance=gm)
    return render(request,'student/update.html',{'form':fm})