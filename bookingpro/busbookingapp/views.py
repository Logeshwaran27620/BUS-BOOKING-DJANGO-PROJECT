from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import razorpay

from busbookingapp.models import buschndpm, busdetails, busmduchn, contactdetails,  passengerdetailsforms1
# from busbookingapp.models import details

# Create your views here.
def user_login(request):
    a={}
    if request.method=='GET':
        return render (request,'login.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        if u=='' or p=='':
            a['err']="feilds are empty"
            return render (request,'login.html',a)
        else:
            b=authenticate(username=u,password=p)
            print('credential',b)
            if b is not None:
                login(request,b)
                return redirect('/1/')
            else:
                a['err']="password and username invalid"
                return render (request,'login.html',a)
            


def regist(request):
    b={}
    if request.method=='POST':
        u=request.POST['uname']
        l=request.POST['lname']
        p=request.POST['upass']
        cp=request.POST['ucpass']
        if u=='' or l=='' or p=='' or cp=='':
            b['err']='the empty feild'
            return render (request,'register.html',b)
        elif p!=cp:
            b['err']='password didnt match'
            return render(request,'register.html',b)            
        else:
            try:
                b['success']="sucessfully register"
                a=User.objects.create(username=u,last_name=l,password=p)
                a.set_password(p)
                a.save()
                return redirect('2/')
            except:
                b['err']="user already"
                return render(request,'register.html',b)
    else:
        return render(request,'register.html',b)     
   

def main(request):
    return render (request,'mainn.html')

def first(request):
    return render (request,'first.html')
# views.py
from django.shortcuts import render, redirect
from .models import  Bookingselection
from django.db.models import Q


from django.shortcuts import render
from .models import Bookingselection
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render
from .models import Bookingselection
@csrf_protect





@csrf_protect
def bookingg(request):
    if request.method == "POST":
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        # passengers = request.POST.get('passengers')
        # depart = request.POST.get('depart')

        # Fetch data from the database based on the selected values
        routes = Bookingselection.objects.filter(origin=origin, destination=destination)

        # Determine the template to redirect to based on the selected values
        if origin == "CHENNAI" and destination == "MADURAI":
             template = 'buschnmdu.html'

        elif origin == "CHENNAI" and destination == "COIMBATORE":
             template = 'buschncbe.html'
        elif origin == "CHENNAI" and destination == "DHARAPURAM":
             template = 'buschndpmm.html'
        

        else:
            # Default template or handle other routes
            template = 'mainn.html'  # Replace with your default template

        # Pass the fetched data to the template
        return render(request, template, {'routes': routes})

    return render(request, 'mainn.html')

        

def chn_mdu(request):
    return render (request,"buschnmdu.html")

def chn_cbe(request):
    return render (request,"buschncbe.html")

def chn_dpm(request):
    return render (request,"buschndpmm.html")

def mdu_chn(request):
    return render (request,"busmduchn.html")


def orderlist(request):
    
    return render (request,"busmduchn.html")



def gallery(request):
    return render (request,"gallery.html")

def chn_dpm(request):
    return render(request, 'buschndpm.html')

def dpm_chn(request):
    return render (request,"busdpmchn.html")

def seatselection(request):
    return render (request,"seat.html")

def bookdetail(request):
   
    if request.method=='POST':
        u=request.POST['ufname']
        n=request.POST['unumber']
        e=request.POST['uemail']
        a=request.POST['uage']
        g=request.POST['ugender']
        c=request.POST['uadult']
        bp=request.POST['ubp']
        dp=request.POST['udp']
        it=request.POST['uidtype']
        i=request.POST['uid']
        s=request.POST['useat']

        a=passengerdetailsforms1.objects.create(username=u,usernumber=n,useremail=e,userage=a,usergender=g,userchild=c,userid=i,userboardingpoint=bp,userdropingpoint=dp,useridtype=it,userseat=s)
        a.save()
        return redirect('/payment/')
    
    else:
        return render(request,'busdetails.html')  
        # return redirect('payment/')
   

def busdb(request):
    context = {}
    details = busdetails.objects.all()  # Retrieve all movies from the database
    context['busdetails'] =details  # Pass movies queryset to the context dictionary
    return render(request, 'seatbook.html', context)

def cat_filter(request,a):
    q1=Q(is_active=True)
    q2=Q(cat=a)
    p=busdetails.objects.filter(q1 & q2)
    b={}
    b['products']=p
    return render (request,'index.html',b)

def busdb1(request):
    context = {}
    details = busmduchn.objects.all()  # Retrieve all movies from the database
    context['busmduchn'] =details  # Pass movies queryset to the context dictionary
    return render(request, 'busmduchn.html', context)

def busdb2(request):
    context = {}
    details = buschndpm.objects.all()  # Retrieve all movies from the database
    context['buschndpm'] =details  # Pass movies queryset to the context dictionary
    return render(request, 'buschndpm.html', context)

def busdb3(request):
    context = {}
    details = buschndpm.objects.all()  # Retrieve all movies from the database
    context['busdpmchn'] =details  # Pass movies queryset to the context dictionary
    return render(request, 'busdpmchn.html', context)





def paymentdetail(request):
    return render (request,"payment.html")



def contact(request):
        
        if request.method=='POST':

            u=request.POST['uname']
            e=request.POST['uemail']
            n=request.POST['unumber']
        
            a=contactdetails.objects.create(username=u,usernumber=n,useremail=e)
            a.save()
            return redirect('/contact/')
    
        else:
            return render(request,'contact.html')

def makepayment(request):
    return render (request,'pay.html')  

    
       


    

              
     


