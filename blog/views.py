from django.contrib import messages
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    comments = Comment.objects.filter(approved_comment=True)
    return render(request, 'blog/post_list.html', {'posts': posts, 'comments': comments})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('comment_added')

    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'save_draft' in request.POST:
                post.published_date = None
                messages.success(request, 'Post salvo como rascunho.')
                post.save()
                return redirect('post_draft_list')  # redireciona para a lista de rascunhos
            else:
                post.published_date = timezone.now()
                messages.success(request, 'Post publicado com sucesso.')
                post.save()
                return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # adicionando request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'save_draft' in request.POST:
                post.published_date = None  # define o post como rascunho
                messages.success(request, 'Post salvo como rascunho.')
                return redirect('post_draft_list')  # redireciona para a lista de rascunhos
            else:
                post.published_date = timezone.now()
                messages.success(request, 'Post publicado com sucesso.')
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def sobre(request):
    return render(request, 'blog/sobre.html')


def sugestao(request):
    return render(request, 'blog/sugestao.html', {})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publicar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publicar()
    return redirect('post_detail', pk=post.pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_draft_list')


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,
                             'Muito obrigado por comentar! Seu comentário será avaliado pela administração e aparecerá em breve.')
            return redirect('add_comment_to_post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def comment_added(request):
    return render(request, 'blog/comment_added.html')
