from django.shortcuts import render, redirect
from service.models import Register

def page(request, template,a=None):
    if not request.session.get("username"):
        return redirect("/login/")
    return render(request, template,a)

def index(request):
    return page(request , "index.html")


def about(request):
    return page(request , "about.html")


def booking(request):
    return page(request , "booking.html")


def contact(request):
    return page(request , "contact.html")


def room(request):
    return page(request , "room.html")


def service(request):
    return page(request , "service.html")


def team(request):
    return page(request , "team.html")


def testimonial(request):
    return page(request , "testimonial.html")

# def login(request):
#     return render(request , "login.html")


def user(request):
    data = Register.objects.all()
    # dictionary
    a = {"data":data}
    return page(request , "user.html", a)

# def register(request):
#     return render(request , "register.html")


def register(request):
    try:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        a1 = Register(username=username, email=email, password=password)
        a1.save()
    
        return redirect("/user/")
        
        # if password == confirm_password:
        #     a1 = Register(username=username, email=email, password=password)
        #     a1.save()
        #     # return render(request, "register.html", {"success": True})
        #     return redirect("/user/")
        # else:
            # If passwords don't match, you can show an error page or redirect back
            # return render(request, "register.html", {"password": True})
       
        # ✅ Print in VS Code terminal
        # print("------ User Registration Data ------")
        # print("Username:", username)
        # print("Email:", email)
        # print("Password:", password)
        # print("Confirm Password:", confirm_password)
        
    except:pass
    return render(request, "register.html")            
        
       
def delete(request, id):
    data = Register.objects.get(id=id)
    data.delete()
    return redirect("/user/")


def update(request, id):
    data = Register.objects.get(id=id)

    if request.method == "POST":
        data.username = request.POST.get("username")
        data.email = request.POST.get("email")
        data.password = request.POST.get("password")
        data.save()
        return redirect("/user/")  # redirect after update

    # For GET request, show the update form
    return render(request, "update.html", {"data": data})
       
        
def login(request):
    if request.session.get("username"):   # already logged in → redirect home
        return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Register.objects.get(username=username, password=password)
            request.session["username"] = user.username 
            return redirect("/")
        except Register.DoesNotExist:
            return redirect("/login/")

    return render(request, "login.html")


def logout(request):
    request.session.flush()  # clear all session data
    return redirect("/login/")  # after logout → go to login
