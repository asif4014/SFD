from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from scholarship.models import Users,StuDetails
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'scholarship/index.html')

def registration(request):
	return render(request,'scholarship/registration.html')

def login(request):
	return render(request,'scholarship/login.html')
    
def form(request):
	return render(request,'scholarship/form.html')
    
def form1(request):
	return render(request,'scholarship/form1.html')
    
def form2(request):
	return render(request,'scholarship/form2.html')

def show(request):
    if request.method=="POST":
        regdno = request.POST["regdno"]
        dob = request.POST["dob"]
        if StuDetails.objects.filter(regdno=regdno,dob=dob):
            stu = StuDetails.objects.get(regdno=regdno)
            context = {'obj':stu}
            return render(request,'scholarship/show.html',context)

        else:
            messages.warning(request,f'OOPS!! Wrong credentials')
            return render(request,'scholarship/form2.html',{messages:messages})

	
def aadharcheck(request):
    regdno = request.GET['regdno']
    aadhar = request.GET['aadhar']

    s1 = StuDetails.objects.get(regdno=regdno)
    if str(s1.aadhar) == aadhar:
        check = 1
    else:
        check = 0

    res = {'final':check}
    return JsonResponse(res)


def usercheck(request):
    name = request.GET['name']
    regdno = request.GET['regdno']

    s1 = Users.objects.get(name=name)
    if str(s1.regdno) == regdno:
        check = 1
    else:
        check = 0

    res = {'final':check}
    return JsonResponse(res)

def saved(request):
    if request.method=="POST":
        name = request.POST["name"]
        course = request.POST["course"]
        regdno = request.POST["regdno"]
        password = request.POST["password"]
        user = Users(name=name,course=course,regdno=regdno, password= password)
        user.save()
        messages.success(request,f'You have successfully registered')
    return render(request,'scholarship/login.html',{messages:messages})

def details(request):
    if request.method=="POST":
        name = request.POST["name"]
        regdno = request.POST["regdno"]
        gender = request.POST.get("gender",'Male')
        dob = request.POST["dob"]
        scholartype = request.POST.get("scholartype",'Gate')
        aadhar = request.POST["aadhar"]
        email  = request.POST["email"]
        contact = request.POST["mobile"]
        stu = StuDetails(name=name,regdno=regdno,gender=gender,dob=dob,scholartype=scholartype,
        aadhar=aadhar,email=email,contact=contact)
        stu.save()
        messages.success(request,f'Congrats!! You have applied for the scholarship')
    return render(request,'scholarship/form.html',{messages:messages})


def authentication(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        if Users.objects.filter(regdno=username,password=password):
            return render(request,'scholarship/form.html')
        else:
            messages.warning(request,f'OOPS!! Wrong password')
            return render(request,'scholarship/login.html',{messages:messages})

            
   

        
