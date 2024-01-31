from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(req):
    return render(req, "index.html")

def browseauction(req):
    return render(req, "browseauction.html")

def mybid(req):
    return render(req, "mybid.html")

def createauction(req):
    return render(req, "createauction.html")

def login(req):
    if req.method == "POST":
            uname = req.POST["uname"]
            upass = req.POST["upass"]
            context = {}
            if uname == "" or upass == "":
                context["errmsg"] = "Field can't be empty"
                return render(req, "login.html", context)
            else:
                username = uname
                userdata = authenticate(username=uname, password=upass)
                context = {"username": username}
                if userdata is not None:
                    login(req, userdata)
                    return redirect("/")
                    #return render(req, "index.html", context)
                else:
                    context["errmsg"] = "Invalid username and password"
                    return render(req, "login.html", context)
    else:
            return render(req, "login.html")


def register(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}
        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "register.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and Confirm Password doesn't match"
            return render(req, "register.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/")
            except Exception:
                context["errmsg"] = "User Already Exists"
                return render(req, "register.html", context)
    else:
        return render(req, "register.html")


def userlogout(req):
    logout(req)
    return redirect("/")