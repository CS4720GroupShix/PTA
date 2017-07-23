from django.shortcuts import render, redirect
from pta.forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Teacher, ParentalUnit, TeamMember
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib import auth

# Create your views here.
from django.http import HttpResponse

@login_required()
def homepage(request):
    # print(request.user)
    # print(request.POST)
    #current_user = auth.get_user(request)
    try:
        parental = ParentalUnit.objects.get(user=request.user)
        teacher = parental.teacher
    except ParentalUnit.DoesNotExist:
        parental = None

    if parental:
        print(parental.user)
        print(parental.teacher)
        return render(request, 'pta/home.html', {'parentalunit': parental, })
    else:
        return render(request, 'pta/home.html')


#@method_decorator(login_required, name='dispatch')
# class HomeView(generic.DetailView):
#     model = ParentalUnit
#     template_name = 'pta/home.html'


# @login_required()
# def meettheteam(request):
#      return render(request, 'pta/meettheteam.html')

@method_decorator(login_required, name='dispatch')
class AboutTeamView(generic.ListView):
    model = TeamMember
    template_name = 'pta/meettheteam.html'


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