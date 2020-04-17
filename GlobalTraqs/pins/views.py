from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponse, HttpResponseRedirect
from .models import pin
from .forms import PostForm
from taggit.models import Tag
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(['POST',])
def setTags(config):
    data = config.data
    tags = data['tags']
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()
    
    context = {
        'form':form,
    }
    return context
    
    if not tags:
        return HttpResponse("empty tags")

@api_view(['GET',])
def getTags():
    posts = pin.objects.order_by('-published')
    common_tags = pin.tags.most_common()[:4]
    context = {
        'posts':posts,
        'common_tags':common_tags,
    }
    return Json(context, JsonRequestBehavior.AllowGet);


def home_view(request):
    posts = pin.objects.order_by('-published')
    # Show most common tags 
    common_tags = pin.tags.most_common()[:4]
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home.html', context)

def detail_view(request, slug):
    post = get_object_or_404(pin, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'detail.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = pin.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)