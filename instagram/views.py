
from django.contrib import messages
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