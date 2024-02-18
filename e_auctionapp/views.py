from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.db.models import Q
from random import sample


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        allproducts = Product.objects.all()
        random_products = sample(list(allproducts), 3)
        context = {"username": user, "allproducts": allproducts, "random_products": random_products}
        return render(request, "index.html", context)
    else:
        allproducts = Product.objects.all()
        random_products = sample(list(allproducts), 3)
        context = {"allproducts": allproducts, "random_products": random_products}
        return render(request, "index.html", context)

def browseauction(request):
    if request.user.is_authenticated:
        user = request.user
        allproducts = Product.objects.all()
        context = {"username": user, "allproducts": allproducts}
        return render(request, "browseauction.html", context)
    else:
        allproducts = Product.objects.all()
        context = {"allproducts": allproducts}
        return render(request, "browseauction.html", context)
    
def searchproduct(req):
    query = req.GET.get("q")
    errmsg = ""
    if query:
        allproducts = Product.objects.filter(
            Q(product_name__icontains=query)
            | Q(category__icontains=query)
            | Q(base_price__icontains=query)
            | Q(desc__icontains=query)
        )
        if len(allproducts) == 0:
            errmsg = "No result found"

    else:
        allproducts = Product.objects.all()

    context = {"allproducts": allproducts, "query": query, "errmsg": errmsg}
    return render(req, "browseauction.html", context)    
    

def createauction(request):
    if request.user.is_authenticated:
        user = request.user
        context = {"username": user}
        return render(request, "createauction.html", context)
    else:
        return render(request, "createauction.html")
    

def mybid(request):
    if request.user.is_authenticated:
        user = request.user
        context = {"username": user}
        return render(request, "mybid.html", context)
    else:
        return render(request, "mybid.html")
    
def myproduct(request):
    if request.user.is_authenticated:
        user = request.user
        context = {"username": user}
        return render(request, "myproduct.html", context)
    else:
        return render(request, "myproduct.html")    



def loginuser(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")
        context = {}
        
        if not uname or not upass:
            context["errmsg"] = "Fields can't be empty"
            return render(request, "login.html", context)
        else:
            user = authenticate(username=uname, password=upass)
            context["username"] = uname
            
            if user is not None:
                login(request, user)  # This line logs the user in
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(request, "login.html", context)
    else:
        return render(request, "login.html")



def register(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")
        ucpass = request.POST.get("ucpass")
        
        context = {}

        if not uname or not upass or not ucpass:
            context["errmsg"] = "Fields can't be empty"
        elif upass != ucpass:
            context["errmsg"] = "Password and Confirm Password don't match"
        else:
            try:
                user = User.objects.create(username=uname)
                user.set_password(upass)
                user.save()
                return redirect("/login")
            except Exception as e:
                context["errmsg"] = str(e)

        return render(request, "register.html", context)
    else:
        return render(request, "register.html")


def userlogout(req):
    logout(req)
    return redirect("/")


def contact(request):
    if request.user.is_authenticated:
        user = request.user
        context = {"username": user}
        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html") 
    

def aboutus(request):
    if request.user.is_authenticated:
        user = request.user
        context = {"username": user}
        return render(request, "aboutus.html", context)
    else:
        return render(request, "aboutus.html")     
    
def product_detail(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        product = get_object_or_404(Product, product_id=product_id)
        context = {"username": user, "product": product}
        return render(request, "product_detail.html", context)
    else:
        return redirect('/login')
    
    