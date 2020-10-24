from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "my_blogs/index.html")


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")  # 这个地方是让所有的topics按日期排列，fliter则是用来确保登陆的用户只可以查看自己的东西
    context = {"topics": topics}
    return render(request, "my_blogs/topics.html", context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    # if topic.owner!=Topic.objects.get(id=topic_id):
    #     raise Http404

    entries = topic.entry_set.order_by("-date_added")  # 这个地方是让按降序排列
    context = {"topic": topic, 'entries': entries}
    return render(request, "my_blogs/topic.html", context)

@login_required
def new_topic(request):
    if request.method != "POST":
        "创建一个新的表单"
        form = TopicForm()

    else:
        form = TopicForm(request._post)

        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return HttpResponseRedirect(reverse("my_blogs:topics"))

    context = {"form": form}
    return render(request, "my_blogs/new_topic.html", context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if topic.owner!=request.user:
        raise Http404

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('my_blogs:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, "my_blogs/new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner!=request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求， 使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据， 对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_blogs:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'my_blogs/edit_entry.html', context)


def about(request):
    return render(request, "my_blogs/about.html")


