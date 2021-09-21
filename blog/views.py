from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm, AddCommentForm
from blog.models import Post, Category, Comment


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = post.total_likes()
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ['title', 'body']

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCatetoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class CategoryPostView(DetailView):
    model = Category
    template_name = 'category.html'

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def searchPost(request):
    if request.method == 'POST':
        search_target = request.POST['search_target']
        posts = Post.objects.filter(title__contains=search_target)
        return render(request,'searchresult.html',
                      {'search_target':search_target,
                       'posts':posts})
    else:
        return render(request, 'searchresult.html', {})


