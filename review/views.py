from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import cinemareview
from .forms import PostForm

def index(req):
    posts = cinemareview.objects.all()
    form = PostForm()
    context = {'posts': posts, 'form': form, }
    return render(req, 'review/index.html', context)

def add(req):
    form = PostForm(req.POST)   
    form.save(commit=True)
    return HttpResponseRedirect(reverse('index'))

def delete(req, id=None):
    review = get_object_or_404(cinemareview, pk=id)
    review.delete()
    return HttpResponseRedirect(reverse('index'))

def update(req, id=None):
    post = get_object_or_404(cinemareview, pk=id)
    form = PostForm()
    context = {'post': post, 'form': form, }
    return render(req, 'review/edit.html', context)

def do_update(req, id=None):
    c = cinemareview.objects.get(pk=id)
    c.review = req.POST["review"]
    c.rate = req.POST["rate"]
    c.save()
    posts = cinemareview.objects.all()
    form = PostForm()
    context = {'posts': posts, 'form': form, }
    return render(req, 'review/index.html',context)
