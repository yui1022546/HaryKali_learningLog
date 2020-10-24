from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.shortcuts import render

from .models import bug_inform
from .forms import BugInfromForm

from django.contrib.auth.decorators import login_required


# def submit(request):
#     """测试用"""
#     return render(request,"bug_submit/submit.html")
@login_required()
def submit(request):
    """正式"""

    if request.method != "POST":
        bug_inform = BugInfromForm()

    else:
        bug_inform = BugInfromForm(request._post)

        if bug_inform.is_valid():
            new_bug = bug_inform.save(commit=False)
            new_bug.bug_owner = request.user
            new_bug.save()
            return HttpResponseRedirect('bug_submit/submit.html')

    context = {'bug_inform': bug_inform}

    return render(request, "bug_submit/submit.html", context)


@login_required()
def discuss(request):
    bug_inform_s = bug_inform.objects.order_by("-date_added")  # 这个地方是让所有的topics按日期排列，fliter则是用来确保登陆的用户只可以查看自己的东西
    context = {"bug_infrom_s": bug_inform_s}
    return render(request, "bug_submit/discuss.html", context)

# def discuss(request):
#     return render(request, "bug_submit/discuss.html")
