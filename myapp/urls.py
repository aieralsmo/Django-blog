from django.conf.urls import url


from .import views

name = 'myapp'
urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^fengmian/$', views.fengmian, name='fengmian'),
	url(r'^about/$', views.about, name='about'),
	url(r'^list/$', views.list, name='list'),
    url(r'^time/$', views.time, name='time'),
	url(r'^detail/$', views.detail, name='detail'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^retrieve/$', views.retrieve, name='retrieve'),
	url(r'^register/$', views.register, name='register'),
	url(r'^upgrate_post/$', views.upgrate_post, name='upgrate_post'),

]