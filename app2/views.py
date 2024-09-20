from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from django.contrib import messages
from . models import Blog, Comment
from . forms import BlogPostForm, CommentPostForm

# Create your views here.
def home(request):
    search = request.GET.get('search')
    msg = None
    
    if search:
        posts = Blog.objects.filter(Q(title__icontains=search) | Q(body__icontains=search) | Q(category__title__icontains=search))
        if not posts.exists():
            msg = 'NO POST'
    else:
        posts = Blog.objects.filter(featured=False)
    
    # Pagination
    pages = Paginator(posts, 4)
    getpage = request.GET.get('page')
    
    try:
        posts = pages.page(getpage)
    except PageNotAnInteger:
        posts = pages.page(1)
    except EmptyPage:
        posts = pages.page(pages.num_pages)
    
    # Safely get the featured post
    featured_post = Blog.objects.filter(featured=True).first()

    context = {
        'posts': posts,
        'featured': featured_post,
        'msg': msg,
        'pages': pages,
    }
    
    return render(request, 'app2/home.html', context)
    
def singlepage(request, slug):
    post = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=post)
    form = CommentPostForm()
    if request.method =='POST':
        if request.user.is_authenticated:
            form = CommentPostForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                messages.success(request, 'Comment submited successfuly')
                return redirect('singlepage', slug=post.slug)
        
    context = {'post':post,'form':form,'comments':comments}
    return render(request, 'app2/singlepage.html',context)



@login_required(login_url='signin')
def create_post(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = slugify(request.POST['title'])
            # blog.slug = slugify(blog.title)
            blog.user = request.user
            blog.save()
            messages.success(request,'Post Created Successfuly')
            return redirect('profile')
    context = {'form':form}
    return render(request, 'app2/post.html', context)


@login_required(login_url='signin')
def update_post(request, slug):
    update = True
    blog = Blog.objects.get(slug=slug)
    form = BlogPostForm(instance=blog)
    if request.method=='POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        blog = form.save(commit=False)
        blog.slug = slugify(request.POST['title'])
        blog.save()
        messages.success(request,'Post Updateded Successfuly')
        return redirect('profile')
    context={'update':update, 'form':form}
    return render(request, 'app2/post.html', context)

@login_required(login_url='signin')  
def delete_post(request, slug):
    blog  = Blog.objects.get(slug=slug) 
    blogs = Blog.objects.filter(user=request.user)
    delete = True
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Post Deleted Successfuly')
        return redirect('profile')
   
    context = {'blog':blog, 'del':delete, 'blogs':blogs}
    return render(request, 'app/profile.html', context)