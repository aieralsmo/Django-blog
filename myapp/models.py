from django.db import models

# Create your models here.


class Post(models.Model):
	"""文章数据表"""

	title 		 = models.CharField(max_length=30, unique=True, verbose_name='标题')
	author 		 = models.CharField(max_length=30, verbose_name='作者')
	bookmark_num = models.IntegerField(default=0, verbose_name='收藏量')
	point_up_num = models.IntegerField(default=0, verbose_name='点赞量')
	is_valid 	 = models.BooleanField(default=1, verbose_name='删除')
	tag 		 = models.CharField(max_length=300, verbose_name='标签')
	img_path 	 = models.CharField(max_length=300, verbose_name='封面路径')
	publish_addr = models.CharField(max_length=200, verbose_name='发布地址')
	publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
	crawl_time 	 = models.DateTimeField(auto_now_add=True, verbose_name='抓取时间')
	content 	 = models.TextField(verbose_name='内容')

	def __str__(self):
		return '{0}'.format(self.title)
	class Meta:
		db_table = 'post'
		
			
class Comment(models.Model):
	"""文章评论表"""

	user_id = models.IntegerField(verbose_name='用户ID')
	post_id = models.IntegerField(verbose_name='文章ID')
	time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
	text    = models.CharField(max_length=500, verbose_name='评论信息')
	class Meta:
		db_table = "comment"
	def __str__(self):
		return '{0}'.format(self.text)


class User(models.Model):
	"""用户表"""
	name 		= models.CharField(max_length=30, unique=True, verbose_name='用户名')
	gender 		= models.BooleanField(default=1, verbose_name='性别')
	age 		= models.IntegerField(default=18, verbose_name='年龄')
	email 		= models.EmailField(max_length=254, verbose_name='邮箱')
	password 	= models.CharField(max_length=30, verbose_name='密码')
	is_valid 	= models.BooleanField(default=1, verbose_name='删除')
	is_master 	= models.BooleanField(default=0, verbose_name='管理员')
	register_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
	update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

	class Meta:
		db_table = "user"
	def __str__(self):
		return '{0}'.format(self.name)