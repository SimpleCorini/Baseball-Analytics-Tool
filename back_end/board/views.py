from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Comment
from .forms import PostForm, CommentForm
from users.models import Profile

@login_required
def analysis(request):
    team_links = [
        {"team": "두산 베어스", "url": "analysis_DOOSAN"},
        {"team": "한화 이글스", "url": "analysis_HANHWA"},
        {"team": "KIA 타이거즈", "url": "analysis_KIA"},
        {"team": "키움 히어로즈", "url": "analysis_KIWOOM"},
        {"team": "KT 위즈", "url": "analysis_KT"},
        {"team": "LG 트윈스", "url": "analysis_LG"},
        {"team": "롯데 자이언츠", "url": "analysis_LOTTE"},
        {"team": "NC 다이노스", "url": "analysis_NC"},
        {"team": "삼성 라이온즈", "url": "analysis_SAMSUNG"},
        {"team": "SSG 랜더스", "url": "analysis_SSG"},
    ]
    context = {"team_links": team_links}
    return render(request, "analysis.html", context)
@login_required
def analysis_DOOSAN(request):
    return render(request, "analysis_DOOSAN.html")
@login_required
def analysis_HANHWA(request):
    return render(request, "analysis_HANHWA.html")
@login_required
def analysis_KIA(request):
    return render(request, "analysis_KIA.html")
@login_required
def analysis_KIWOOM(request):
    return render(request, "analysis_KIWOOM.html")
@login_required
def analysis_KT(request):
    return render(request, "analysis_KT.html")
@login_required
def analysis_LG(request):
    return render(request, "analysis_LG.html")
@login_required
def analysis_LOTTE(request):
    return render(request, "analysis_LOTTE.html")
@login_required
def analysis_NC(request):
    return render(request, "analysis_NC.html")
@login_required
def analysis_SAMSUNG(request):
    return render(request, "analysis_SAMSUNG.html")
@login_required
def analysis_SSG(request):
    return render(request, "analysis_SSG.html")
@login_required
def analysis_result(request):
    return render(request, "analysis_result.html")



@login_required
def predictions(request):
    return render(request, "predictions.html")

@login_required
def predictions_result(request):
    return render(request, "predictions_result.html")


@login_required
def matchups(request):
    return render(request, "matchups.html")

@login_required
def matchups_result(request):
    return render(request, "matchups_result.html")


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
