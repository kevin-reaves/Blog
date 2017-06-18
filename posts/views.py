from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
import os


# Create your views here.
def home(request):

    posts = Post.objects.order_by('-pub_date')

    return render(request, 'posts/home.html', {'posts':posts})

def about(request):
    return render(request, 'posts/about.html')

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_details.html', {'post':post})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body']:
            post = Post()
            post.title = request.POST['title']
            post.pub_date = timezone.datetime.now()

            #ignores the error from not submitting an image
            #models.py contains a default, that will be used
            try:
                post.image = request.FILES['image']

                #ImageField filtering wasn't working, so I had to filter it here
                filename, file_extension = os.path.splitext(post.image.name)
                acceptedFiletypes = ['.gif', '.jpeg', '.jpg', '.png', '.svg', '.bmp']
                #Uppercase extensions are valid
                if file_extension.lower() not in acceptedFiletypes:
                    return render(request, 'posts/create.html',
                                  {'error': 'Error: Please submit an image file.'})


            except MultiValueDictKeyError:
                pass

            post.body = request.POST['body']
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            #If the user didn't include a title or body
            return render(request, 'posts/create.html',
                          {'error': 'Error: You must include a title and a body to create a post.'})
    else:
        return render(request, 'posts/create.html')