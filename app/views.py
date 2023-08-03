from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def Home(request):
    if request.session.get('Username'):
        username=request.session.get('Username')
        d={'username':username}
        return render(request,'Home.html',d)

    return render(request,'Home.html')

def Register(request):
    d={'UFO':UserForm(),'PFO':ProfileForm()}
    if request.method == 'POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUFO=UFD.save(commit=False)
            NSPFO=PFD.save(commit=False)
            NSUFO.set_password(UFD.cleaned_data['password'])
            NSUFO.save()
            NSPFO.username=NSUFO
            NSPFO.save()
            send_mail('registration process','your registration is sucessful',
                      'shivaramraj8804@gmail.com',[NSUFO.email],
                      fail_silently=False)
            return HttpResponse('data inserted sucessfully')
        else:
            return HttpResponse('invalid data')

    return render(request,'register.html',d)

def User_login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        AO=authenticate(username=username,password=password)
        if AO and AO.is_active:
            login(request,AO)
            request.session['Username']=username
            return HttpResponseRedirect(reverse('Home'))
        else:
            return HttpResponse('invalid user credentials')
    return render(request,'Login.html')


@login_required
def User_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('Home'))


@login_required
def Display_profile(request):
    username=request.session.get('Username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'Dispaly_profile.html',d)



@login_required
def Change_password(request):
    if request.method=='POST':
        username=request.session.get('Username')
        pw=request.POST['pw']
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('password changed sucessfully')
    return render(request,'Change_password.html')


def forgetpassword(request):
    if request.method == 'POST':
        un=request.POST['un']
        pw=request.POST['pw']
        UO=User.objects.filter(username=un)
        if UO:
            UO[0].set_password(pw)
            UO[0].save()
            return HttpResponse('password is updated sucessfully ')
        else:
            return HttpResponse('user name is not avilable in database')
    return render(request,'forgetpassword.html')