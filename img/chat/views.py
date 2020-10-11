from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import CommentForm, PostForm
from .models import Post


@login_required
def home(request):
	""" The home news feed page """

	# Get users whose posts to display on news feed and add users account
	_users = list(request.user.followers.all())
	_users.append(request.user)

	# Get posts from users accounts whose posts to display and order by latest
	posts = Post.objects.filter(user__in=_users).order_by('-posted_date')
	comment_form = CommentForm()
	return render(request, 'chat/home.html', {'posts': posts, 'comment_form': comment_form})
