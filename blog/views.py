from django.shortcuts import render, get_object_or_404 #shortcuts there by default
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                   )
#from django.http import HttpResponse

#this is where logic goes for certain routes

#adding a list of dicts. these are just staic. Not used as of part5, where we repalced it with DB data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted:': 'August 27,2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted:': 'August 28,2018'
    }
]

#part 5 replace the posts static stuff to get things from our db

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #3rd param is passed to the template and the template can access it
    #goes to templates directory by default, though you have to make the dir
    #HttpResponse('<h1>Blog Home</h1>')

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


#Part 10 class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # looks for template with this naming convention <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # looks for template with this naming convention <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #inherits from the LoginRequiredMixin that we imported
    model = Post
    fields = ['title', 'content']

    #need to override form_vaild method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #inherits from the LoginRequiredMixin that we imported
    model = Post
    fields = ['title', 'content']

    #need to override form_vaild method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
