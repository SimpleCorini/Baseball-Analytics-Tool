from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Comment
from .forms import PostForm, CommentForm
from users.models import Profile


@login_required
def article_list(request):
    article_list = Article.objects.order_by("-reg_date")

    # 요청에서 'page' 매개변수를 받아옴, 기본값은 1
    page = request.GET.get("page", 1)
    paginator = Paginator(article_list, 10)
    articles = paginator.get_page(page)

    context = {'article_list': articles}
    return render(request, "article_list.html", context)


@login_required
def article_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            profile = get_object_or_404(Profile, user=request.user)
            article.nickname = profile.nickname
            article.type_team = form.cleaned_data['team']
            article.count = 0
            print('작성자:', article.nickname, '제목 : ', article.title, '내용:', article.content, "팀 분류 :", article.type_team)
            article.save()
            return redirect('article_list')
        else:
            print("Error")
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'article_create.html', context)
@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(post=article).order_by('reg_date')
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'article.html', context)

@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = article
            profile = get_object_or_404(Profile, user=request.user)
            comment.nickname = profile.nickname
            comment.save()
            return redirect('article_detail', pk=article.pk)
    return redirect('article_detail', pk=article.pk)