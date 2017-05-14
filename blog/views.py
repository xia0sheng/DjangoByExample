from blog.models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status = 'published',
                             published__year=year,
                             published__month=month,
                             published_day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})