from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from instagram.forms import PostForm
from instagram.models import Post

@login_required
def index(request):

    timesince = timezone.now() - timedelta(days=3)
    post_list = Post.objects.all().filter(
        Q(author=request.user) |
        Q(author__in=request.user.following_set.all())
    ).filter(
        created_at__gte=timesince
    )

    suggested_user_list = get_user_model().objects.all().exclude(pk=request.user.pk).exclude(pk__in=request.user.following_set.all())[:3]

    request.user.following_set.all()

    return render(request, "instagram/index.html", {
        "post_list": post_list,
        "suggested_user_list": suggested_user_list,
    })


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, "포스팅을 저장했습니다.")
            # return redirect(reverse("root"))
            return redirect(post)
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {
        "form": form,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # comment_form = CommentForm()
    return render(request, "instagram/post_detail.html", {
        "post": post,
        # "comment_form": comment_form,
    })


def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)

    # 접속한 유저와 확인하는 유저가 팔로우가 되있는지 체크
    if request.user.is_authenticated:
        is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
    else:
        is_follow = False

    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # 실제 데이터베이스에 count 쿼리를 던짐
    # len(post_list) # post리스트를 다 가져와서 메모리에 얹진다음에 리스트의 개수를 반환
    return render(request, 'instagram/user_page.html', {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
        "is_follow": is_follow,
    })
