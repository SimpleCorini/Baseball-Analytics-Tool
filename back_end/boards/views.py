from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.contrib.contenttypes.models import ContentType

from .models import Article, Comment,Like
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
    return render(request, "boards/article_list.html", context)


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
    return render(request, 'boards/article_create.html', context)


@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 조회수 증가
    article.count = F('count') + 1
    article.save(update_fields=['count'])
    article.refresh_from_db()  # 실시간으로 증가된 조회수를 반영하기 위해

    comments = Comment.objects.filter(post=article).order_by('reg_date')
    comment_form = CommentForm()

    article_content_type = ContentType.objects.get_for_model(Article)
    comment_content_type = ContentType.objects.get_for_model(Comment)

    article_liked = Like.objects.filter(
        user=request.user,
        content_type=article_content_type,
        object_id=article.pk
    ).exists()

    comment_likes = {
        comment.pk: Like.objects.filter(
            user=request.user,
            content_type=comment_content_type,
            object_id=comment.pk
        ).exists() for comment in comments
    }

    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'article_liked': article_liked,
        'comment_likes': comment_likes,
        'edit_comment_id': None,  # 수정 중인 댓글 ID
    }
    return render(request, 'boards/article.html', context)

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.nickname == request.user.profile.nickname:
        article.delete()
        print("게시글이 성공적으로 삭제되었습니다.")

    return redirect('article_list')

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.nickname != request.user.profile.nickname:
        return redirect('article_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = PostForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'boards/article_edit.html', context)



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


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.nickname == request.user.profile.nickname:
        comment.delete()
        print("댓글이 성공적으로 삭제되었습니다.")

    return redirect('article_detail', pk=comment.post.pk)

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.nickname != request.user.profile.nickname:
        return redirect('article_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    comments = Comment.objects.filter(post=comment.post).order_by('reg_date')
    context = {
        'article': comment.post,
        'comments': comments,
        'comment_form': form,
        'edit_comment_id': comment.id,
    }
    return render(request, 'boards/article.html', context)


@login_required
def toggle_like(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    content_object = content_type.get_object_for_this_type(pk=object_id)
    like, created = Like.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id
    )
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    # 좋아요 수 가져오기
    content_object.refresh_from_db(fields=['like_count'])

    return HttpResponse(status=204)
