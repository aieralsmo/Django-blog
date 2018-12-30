from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# Create your views here.

import json
from .models import Post,User,Comment
from .utils import pagination_handle

def index(request):

	posts = Post.objects.all()[0:10]
	
	
	r_recommend_posts = Post.objects.filter(point_up_num=0)[0:10]

	r_latest_posts = Post.objects.filter(publish_time__year='2018')[0:10]

	return render(request, 'myapp/reference/index.html',
		{
			'posts':posts,
			'r_latest_posts':r_latest_posts,
			'r_recommend_posts':r_recommend_posts
		})

def fengmian(request):
	return render(request, 
		'myapp/reference/fengmian.html'
		)

def about(request):
	return render(request,
		'myapp/reference/about.html'
		)

def list(request):

	if request.method == "POST":
		kw = request.POST.get('keyboard')
		posts = Post.objects.filter(title__contains=kw)
		if not bool(len(posts)):
			posts = Post.objects.filter(content__contains=kw)
	else:
		tag = request.GET.get('tag')
		if tag is not None:
			posts = Post.objects.filter(tag__contains=tag)
		else:
			posts = Post.objects.all()

	p = pagination_handle(request,obj=posts,size=10)
	return render(request, 
		'myapp/reference/list.html',{
		'null':len(posts),
		'posts':p
	})

def time(request):
	posts = Post.objects.filter(publish_time__year__gte=(2015))
	p = pagination_handle(request,obj=posts,size=20)
	return render(request, 'myapp/reference/time.html',{'posts':p})

def login(request):
	if request.is_ajax():
		if 'user' in request.session:
			return HttpResponse(200)
		account = request.POST.get('account')
		password = request.POST.get('password')
		user = User.objects.filter(name=account,password=password).first()
		
		if bool(user):
			request.session['user'] = str(user)
			# session 失效时间为2小时
			request.session.set_expiry(7200) 
			return HttpResponse(200)
		return HttpResponse('!200')

def logout(request):
	if request.is_ajax():
		if 'user' in request.session:
			request.session.flush()
			return HttpResponse(200)
		return HttpResponse('!200')

def retrieve(request):
	if request.is_ajax():
		account = request.POST.get('account')
		password = request.POST.get('password')
		user = User.objects.filter(name=account).first()
		if user is not None:
			user.password = password
			user.save()
			return HttpResponse(200)
		return HttpResponse('!200')

def register(request):
	if request.is_ajax():
		account = request.POST.get('account')
		password = request.POST.get('password')
		
		user = User()
		user.name = account
		user.password = password
		try:
			user.save()
		except Exception as e:
			return HttpResponse('!200')
		return HttpResponse(200)

def detail(request):
	if request.method == "GET":
		pid = int(request.GET.get('pid'))
		post = Post.objects.filter(pk=pid).first()
		comm = Comment.objects.filter(post_id=pid)
		count = comm.count()

		total = Post.objects.all().count()

		# 构造上一条信息
		be_id = pid-1 if pid>1 and total > 1 else pid
		bp = Post.objects.filter(pk=be_id).first()
		# 构造下一条信息
		nt_id = pid+1 if pid < total else pid
		np= Post.objects.filter(pk=nt_id).first()

		# 评论区
		c_data = []
		# 神评论
		c_all = Comment.objects.filter(post_id=pid)
		for c in c_all:
			user = User.objects.filter(pk=c.user_id).first().name
			
			dt={
				'user':user,
				'text':c.text,
				'time':c.time
			}
			c_data.append(dt)
		#############################################
	
		if post is None:
			return HttpResponse("""<center><h1>很抱歉，您要访问的页面不存在！</h1>
									<h2>温馨提示：</h2></br>
									请检查您访问的网址是否正确</br>
									如果您不能确认访问的网址，请浏览百度更多页面查看更多网址。</br>
									回到顶部重新发起搜索</br>
									如有任何意见或建议，请及时反馈给我们。</center>
								""")


	return render(request, 
		'myapp/reference/info.html',{
		'post':post,
		'count':count,
		'np':np,
		'bp':bp,
		'c_data':c_data
		})

def upgrate_post(request):
	# 登录状态下才能做评论

	if request.is_ajax():
		if request.method == "POST":
			option = request.POST.get('option')
			post_id = int(request.POST.get("post_id"))
			
			if option == "comment":
				text = request.POST.get("text")
				user = request.session.get('user')
				cot = Comment()
				u_id = User.objects.filter(name=user).first().id
				cot.post_id = post_id
				cot.user_id = u_id
				cot.text = text
				cot.save()
			elif option == "point":
				post = Post.objects.filter(pk=post_id).first()
				old_num = post.point_up_num
				current_num = old_num + 1
				post.point_up_num = current_num
				post.save()

			elif option == "bookmark":
				post = Post.objects.filter(pk=post_id).first()
				old_num = post.bookmark_num
				current_num = old_num + 1
				post.bookmark_num = current_num
				post.save()	

	return HttpResponse('')


