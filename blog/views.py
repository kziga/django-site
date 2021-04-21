from django.shortcuts import render

# Create your views here.

# This is what gets executed when the view post_list is requested
def post_list(request):
	return render(request,'blog/post_list.html',{})