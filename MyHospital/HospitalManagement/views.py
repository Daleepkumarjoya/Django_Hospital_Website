from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HomeModel, ServicesModel, AboutModel, DoctorsModel, BookModel, ReviewModel, ContactModel, \
    commentModel
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator


# Create your views here.


def HomePage(request):
    ModelData = HomeModel.objects.all()
    HomeParams = {'ModelData': ModelData}
    return render(request, "HomePage.html", HomeParams)


def servicePage(request):
    ServiceData = ServicesModel.objects.all()
    P = Paginator(ServiceData, 3)
    pageNumber = request.GET.get('page')
    ServiceDataFinal = P.get_page(pageNumber)
    totalpage = ServiceDataFinal.paginator.num_pages
    ServiceDataParams = {'ServiceData': ServiceDataFinal, 'lastpage': totalpage,
                         'totalPageNumber': [n + 1 for n in range(totalpage)]}
    return render(request, "ServicePage.html", ServiceDataParams)


def readMore(request, slug):
    More = ServicesModel.objects.get(Service_slug=slug)
    return render(request, "readMore.html", {'More': More})


def aboutPage(request):
    AboutData = AboutModel.objects.all()
    AboutDataParams = {'AboutData': AboutData}
    return render(request, "aboutPage.html", AboutDataParams)


def doctorPage(request):
    DoctorData = DoctorsModel.objects.all()
    if request.method == 'GET':
        st = request.GET.get('Doctor_name')
        if st != None:
            DoctorData = DoctorsModel.objects.filter(DoctorName__icontains=st)
    DoctorParams = {'DoctorData': DoctorData}
    return render(request, "doctorsPage.html", DoctorParams)


def bookPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        date = request.POST.get('date')
        if name is None and number is None and date is None:
            messages.info(request, "Name,Number and Date Can not be empty")
        else:
            BookData = BookModel(name=name, number=number, email=email, date=date)
            BookData.save()
            messages.success(request, "You Order Is Booked Successfully")
    return render(request, "bookPage.html")


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        comment = commentModel(comment=comment, user=user)
        comment.save()
        messages.success(request, "Your Comments has been Posted Successfully.")
    return render(request, "reviewPage.html")


def Comment(request):
    ReadComments = commentModel.objects.all()
    Readparams = {'ReadComments': ReadComments}
    return render(request, "reviewPage.html", Readparams)


def contactus(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        contactModel = ContactModel(first_name=first_name, last_name=last_name, email=email, number=number,
                                    message=message)
        contactModel.save()
        messages.info(request, "Thank You For Contact Us We Will Reply you Soon.")
    return render(request, "contactPage.html")


def signup(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=user_name).exists():
            messages.info(request, "user Name Exist")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email Exist")
        else:
            user = User.objects.create_user(username=user_name, email=email, password=password)
            user.save()
            return redirect('/Login')
    return render(request, "signupPage.html")


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "User Logged In")
            return redirect("/")
        else:
            messages.info(request, "Invalid Credential")
    return render(request, "LoginPage.html")


def LogOut(request):
    auth.logout(request)
    return redirect('/')
