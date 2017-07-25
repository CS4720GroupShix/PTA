from django.shortcuts import render, redirect
from pta.forms import SignUpForm, AddHomeworkForm, AddWishlistForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Teacher, ParentalUnit, TeamMember, Homework, WishlistItem
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib import auth
from datetime import date

# Create your views here.
from django.http import HttpResponse

#@method_decorator(login_required, name='dispatch')
# class HomeView(generic.DetailView):
#     model = ParentalUnit
#     template_name = 'pta/home.html'

@login_required()
def homepage(request):
    # print(request.user)
    # print(request.POST)
    #current_user = auth.get_user(request)

    myContext = {}
    try:
        parental = ParentalUnit.objects.get(user=request.user)
    except ParentalUnit.DoesNotExist:
        parental = None
    if parental:
        parentlist = ParentalUnit.objects.filter(teacher=parental.teacher)
        myContext = {'parentalunit': parental, 'teacher': parental.teacher, 'parentlist': parentlist,}
    else:
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            teacher = None
        if teacher:
            parentlist = ParentalUnit.objects.filter(teacher=teacher)
            myContext = {'teacher': teacher, 'parentlist': parentlist,}

    myContext['nbar'] = 'home'
    return render(request, 'pta/home.html', myContext)

@login_required()
def wishlist(request):
    myContext = {}
    myContext['nbar'] = 'wishlist'

    if request.method == 'POST':
        try:
            parental = ParentalUnit.objects.get(user=request.user)
        except ParentalUnit.DoesNotExist:
            parental = None

        if parental:
            wishlist = WishlistItem.objects.filter(teacher=parental.teacher, received=False)
            myContext['teacherof'] = parental.teacher
            myContext['parental'] = parental
            myContext['wishlist'] = wishlist

            print("testing we got here")
            id_list = request.POST.getlist('wishchk')
            WishlistItem.objects.filter(id__in=id_list).update(parentalUnit=parental)
            WishlistItem.objects.filter(parentalUnit=parental).exclude(id__in=id_list).update(parentalUnit=None)
            # for wish in wishlist:
            #     chkid = 'chk' + str(wish.id)
            #     print(chkid)
            #     is_checked = request.POST.get(chkid, False)
            #     print(is_checked)

    else:
        try:
            parental = ParentalUnit.objects.get(user=request.user)
        except ParentalUnit.DoesNotExist:
            parental = None

        if parental:
            wishlist = WishlistItem.objects.filter(teacher=parental.teacher, received=False)
            myContext['teacherof'] = parental.teacher
            myContext['parental'] = parental
            myContext['wishlist'] = wishlist
        else:
            try:
                teacher = Teacher.objects.get(user=request.user)
            except Teacher.DoesNotExist:
                teacher = None

            if teacher:
                wishlist = WishlistItem.objects.filter(teacher=teacher)
                myContext['wishlist'] = wishlist
                myContext['teacher'] = teacher

    return render(request, 'pta/wishlist.html', myContext)

@login_required()
def addwishlist(request):

    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None

    if not teacher:
        return HttpResponse("Invalid directory")

    else:
        myContext = {}
        myContext['nbar'] = 'wishlist'
        myContext['teacher'] = teacher

        if request.method == 'POST':
            form = AddWishlistForm(request.POST)
            myContext['form'] = form

            if form.is_valid():
                newWishlistItem = WishlistItem(
                     description = form.cleaned_data['description'],
                     teacher = teacher,
                     received = False,
                )
                newWishlistItem.save()
                return redirect('addwishlist')
        else:
            form = AddWishlistForm()
            myContext['form'] = form

    return render(request, 'pta/addwishlist.html', myContext)









@login_required()
def homework(request):
    myContext = {}
    if request.method == 'POST':
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            teacher = None

        if not teacher:
            return HttpResponse("Permission denied")
        else:
            form = AddHomeworkForm(request.POST)
            if form.is_valid():
                print("Thinks form is valid")
                #fields = ('title', 'description', 'date_assigned', 'due_date', 'points',)
                # newhomework = Homework(
                #     title = form.cleaned_data['title'],
                #     description = form.cleaned_data['description'],
                #     date_assigned = form.cleaned_data['date_assigned'],
                #     due_date = form.cleaned_data['due_date'],
                #     points = form.cleaned_data['points'],
                #     teacher = teacher
                # )
                # newhomework.save()
                return redirect('homework')
    else:
        try:
            parental = ParentalUnit.objects.get(user=request.user)
        except ParentalUnit.DoesNotExist:
            parental = None

        if parental:
            homeworkList = Homework.objects.filter(teacher=parental.teacher)
            myContext['homeworkList'] = homeworkList
        else:
            try:
                teacher = Teacher.objects.get(user=request.user)
            except Teacher.DoesNotExist:
                teacher = None

            if teacher:
                homeworkList = Homework.objects.filter(teacher=teacher)
                myContext['homeworkList'] = homeworkList
                myContext['teacher'] = teacher

        myContext['nbar'] = 'homework'
        myContext['hwtoday'] = date.today()

    return render(request, 'pta/homework.html', myContext)


@login_required()
def addhomework(request):

    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None

    if not teacher:
        return HttpResponse("Invalid directory")

    else:
        myContext = {}
        myContext['nbar'] = 'homework'
        myContext['hwtoday'] = date.today()
        myContext['teacher'] = teacher

        if request.method == 'POST':
            form = AddHomeworkForm(request.POST)
            myContext['form'] = form

            if form.is_valid():
                newhomework = Homework(
                     title = form.cleaned_data['title'],
                     description = form.cleaned_data['description'],
                     date_assigned = form.cleaned_data['date_assigned'],
                     due_date = form.cleaned_data['due_date'],
                     points = form.cleaned_data['points'],
                     teacher = teacher
                )
                newhomework.save()
                return redirect('addhomework')
        else:
            form = AddHomeworkForm()
            myContext['form'] = form

    return render(request, 'pta/addhomework.html', myContext)

@login_required()
def meettheteam(request):
    myContext = {}
    try:
        teammember_list = TeamMember.objects.all()
    except ParentalUnit.DoesNotExist:
        teammember_list = None

    if teammember_list:
        myContext['teammember_list']=teammember_list
    myContext['nbar'] = 'meettheteam'
    return render(request, 'pta/meettheteam.html', myContext)

# @method_decorator(login_required, name='dispatch')
# class AboutTeamView(generic.ListView):
#     model = TeamMember
#     template_name = 'pta/meettheteam.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            theuser = form.save()
            teach = form.cleaned_data.get('teacher')

            parentalunit = ParentalUnit(
                user=theuser,
                teacher=teach,
            )
            parentalunit.save()
#           ParentalUnit.objects.create(user=theuser, teacher=teach)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'pta/signup.html', {'form': form})

@login_required()
def todo(request):
    myContext = {}
    myContext['nbar'] = 'todo'
    return render(request, 'pta/todo.html', myContext)

# def startpage(request):
#      return render(request, 'pta/index.html')
#    return HttpResponse("Hello, world. You're at the PTA index.")

#def startpage(request):
#     print("login_user", request)
#      messages = []
#      if request.method == 'POST':
#          print("POST method")
#          form = LoginForm(request.POST)
#         if form.is_valid():
#             print("form is valid", form)
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('user_detail', args=[user.id]))
#             else:
#                 messages.append('Invalid login')
#         else:
#             messages.append('Login data incomplete')
#     else:
#         form = LoginForm()
#     return render(request, 'clubs/login.html', {'form': form, 'messages': messages})


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]