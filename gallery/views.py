from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def gallery(request):
    posts = Post.objects.all()
    return render(request, 'gallery/gallery.html', {'posts': posts})
def drawing(request):
    posts = Post.objects.all().filter(drawing_or_design='drawing')
    return render(request, 'gallery/drawing.html', {'posts': posts})
def design(request):
    posts = Post.objects.filter(drawing_or_design='design')
    return render(request, 'gallery/design.html', {'posts': posts})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_absolute_url())
        
    else:
        form = PostForm()
    
    context = {
        'form': form,
    }

    # title = request.POST.get('title')
    # image = request.POST.get('image')
    # publishing_date = request.POST.get('publishing_date')
    # Post.objects.create(title=title, image=image, publishing_date=publishing_date)

    return render(request, 'gallery/create.html', context)
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'gallery/detail.html', context)
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("gallery:gallery")