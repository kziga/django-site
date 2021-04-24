from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

# This is what gets executed when the view post_list is requested
def post_list(request):
	posts = Post.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})
