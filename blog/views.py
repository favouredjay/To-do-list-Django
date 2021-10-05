from django.core.checks import messages
from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post


def home_page(request):
    post = Post.objects.all()
    context = {
        "posts": post
    }
    return render(request, 'home.html', context)


def add(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                "error": form.errors
            }
            return render(request, "error_page.html", context)
    else:
        return render(request, 'add.html', context={"form": form})


def update_task(request, pk):
    task = Post.objects.get(id=pk)

    form = PostForm(instance=task)

    if request.method == "POST":
        form = PostForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "update_task.html", {"task_edit_form": form})


def delete(request, pk):
    task = Post.objects.get(id=pk)
    task.delete()
    return redirect("home")

# Create your views here.
