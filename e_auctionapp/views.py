from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product, Bid
from django.db.models import Q
from random import sample
from e_auctionapp.forms import AuctionForm
from .forms import BidForm



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        allproducts = Product.objects.exclude(userid=user)
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
        allproducts = Product.objects.exclude(userid=user)
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

        if request.method == 'POST':
            form = AuctionForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.userid = user  # Set the userid to the currently logged-in user
                product.save()
                return redirect('myauctions')  # Redirect to a page showing the user's products or another appropriate page
        else:
            form = AuctionForm()

        context = {"username": user, "form": form}
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
    
def myauctions(request):
    if request.user.is_authenticated:
        user = request.user
        auctions = Product.objects.filter(userid=user)

        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            status = request.POST.get('status')

            product = get_object_or_404(Product, pk=product_id, userid=user)
            product.status = status
            product.save()

        context = {"username": user, "auctions": auctions}
        return render(request, "myauctions.html", context)
    else:
        return redirect('/login')    



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
        product = get_object_or_404(Product, pk=product_id)
        bid_history = Bid.objects.filter(product=product).order_by('-timestamp')[:2]

        if request.method == 'POST':
            form = BidForm(product_base_price=product.base_price, data=request.POST)
            if form.is_valid():
                bid_amount = form.cleaned_data['bid_amount']

                # Validate bid amount
                if not bid_history and bid_amount <= product.base_price:
                    form.add_error('bid_amount', 'The first bid must be greater than the base price.')
                elif bid_history and bid_amount <= bid_history[0].amount:
                    form.add_error('bid_amount', 'Bid amount must be greater than the previous bid.')

                if not form.errors:
                    new_bid = Bid(product=product, user=user, amount=bid_amount)
                    new_bid.save()
                    product.current_bid = bid_amount
                    product.save()
                    return redirect('product_detail', product_id=product_id)

        else:
            form = BidForm(product_base_price=product.base_price)

        context = {
            "username": user,
            "product": product,
            "bid_history": bid_history,
            "form": form,
        }

        return render(request, "product_detail.html", context)
    else:
        return redirect('/login')
    