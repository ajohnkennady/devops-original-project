from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login

from .models  import Blood,Hospital,Confirmrequest




def home(request):
    return  render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        # if form.is_valid():
            username = request.POST.get('nm')
            password = request.POST.get('pass')
            hospitalname = request.POST.get('hos')
            user = Hospital.objects.create_user(username=username, password=password, hospitalname=hospitalname)
            user.save()
            auth_login(request, user)
            return redirect('home')
    return render(request,"registration.html")
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('nm')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('home')
   



def location(request):
    if request.method == "POST":
        loc = request.POST.get('search')
        locations = Blood.objects.filter(loaction=loc)  
        print(locations)
        return render(request,'home.html', {'location': locations})

    return render(request, 'home.html')


def details(request,userId, location):
        detail = Blood.objects.filter(user_id=userId, loaction=location)
        if detail.exists():
            hname = detail.first()
        blood = []    
        for a in detail:
            blood.append(a.bloodgroupname)

        blood_dict = {bt.replace('+', 'p').replace('-', 'n'): 'rgb(0, 255, 0)' for bt in blood}
        blood_dict.update({'detail': detail, 'hname': hname})
        print(blood_dict)   
        return render(request,'view.html', blood_dict)

   

def Rise(request):
        if request.method=='POST':
        
            id = request.POST.get('text')
            nm = request.POST.get('nm')
            contact = request.POST.get('contact')
            bloodname = request.POST.get('bloodname')
        
            
            confirm_request = Confirmrequest(
                userid=id,
                name=nm,
                contact=contact,
                bloodgroup=bloodname,
                accept=None  # You can set this to a defausssssssswlt value if needed
            )
            confirm_request.save()

            context={'confirm_request':confirm_request}
            return render(request,'home.html')
        
        return render(request,'details.html')


# def Accept(request):

#     value=Confirmrequest.objects.filter(userid = request.user.id)
#     context={'value':value}
#     return render(request,'notific.html',context)

def Accept(request):
    value = Confirmrequest.objects.filter(userid=request.user.id, bloodgroup__isnull=False).exclude(bloodgroup='')
    context = {'value': value}
    return render(request, 'notific.html', context)



def notify(request,value,id):
  
    person=Confirmrequest.objects.get(id=id)
    person.accept = value
    person.save()
    value=Confirmrequest.objects.filter(id = request.user.id)
    context={'value':value}
    return render(request, 'notific.html', context)

def add_blood(request):
    print(1)
    if request.method=="POST":
        print(2)
        blood=request.POST.get('blood')
        location=request.POST.get('loc')
         
        value=Blood(bloodgroupname=blood,user = request.user,loaction=location)
        value.save()

        # context={'value':value}

    return render(request,'nav.html')


