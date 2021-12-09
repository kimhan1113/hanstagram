
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from instagram.forms import PostForm
from instagram.models import Post


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
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # 실제 데이터베이스에 count 쿼리를 던짐
    # len(post_list) # post리스트를 다 가져와서 메모리에 얹진다음에 리스트의 개수를 반환
    return render(request, 'instagram/user_page.html', {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
    })
