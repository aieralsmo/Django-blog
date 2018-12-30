from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def pagination_handle(request,obj,size=10):

	paginator = Paginator(obj,size)#实例化一个分页对象

	page = request.GET.get('page') #获取到页码

	try:
		q = paginator.page(page) #获取某夜对应的记录
	except PageNotAnInteger: #如果页码不是个整数
		q = paginator.page(1)#取第一页的记录
	except EmptyPage:#如果页码太大
		q = paginator.page(paginator.num_pages)#取最后一页的记录
	return q
	