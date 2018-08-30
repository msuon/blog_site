from django.shortcuts import render

from .models import Post
import mistune
md_parser = mistune.Markdown()

# Create your views here.

def index_view(request):
    context = {'greeting': "Welcome to Moniroth Suon's Blog!"}
    return render(request, "blog/index.html", context)

def blog_list_view(request):
    posts = Post.objects.order_by("-pub_date")
    context = {'post_list': posts}
    return render(request, "blog/post_list.html", context)

def blog_page_view(request):
    # Todo: verify that the get methods are working for those
    # post_date = request.GET.get('date')
    post_title = request.GET.get('title')
    # print(post_date)
    print(post_title)
    blog_post = Post.objects.get(title=post_title)
    image_list = blog_post.image_set.all()

    # Prepare content 
    content = md_parser(blog_post.text)
    context = {'blog_post': blog_post,
               'images': image_list,
               'content': content}
    return render(request, "blog/post_page.html", context)

def resume_view(request):
    return render(request, "blog/resume_page.html", {"text": "My Resume Goes Here!"})
