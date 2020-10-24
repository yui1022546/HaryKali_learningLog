from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def logout_view(request):
    """注销用户"""

    logout(request)
    return HttpResponseRedirect(reverse("my_blogs:index"))


def register(request):

    if request.method != "POST":
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():

            new_users = form.save()
            authenticated_user = authenticate(username=new_users.username,
                                              password=request.POST["password1"])


            login(request, authenticated_user)

            return HttpResponseRedirect(reverse("my_blogs:index"))

    context = {"form": form}

    return render(request, "users/register.html", context)
