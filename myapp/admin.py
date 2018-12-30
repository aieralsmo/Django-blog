from django.contrib import admin

# Register your models here.
from .models import User, Post, Comment



@admin.register(User)
class UserAdmin(admin.ModelAdmin):


    def gender(self):
        if self.gender:
            return '男'
        else:
            return '女'
    def isdelete(self):
        if self.is_valid:
            return '是'
        else:
            return '否'

    # 列表页属性
    list_display = ['pk', 'name', 'age', 'password' ,gender , 'register_time',isdelete]
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 5

    # 添加，修改页属性
    # fields = ['gname','ggirlnum','gboynum','gdate','isDelete']
    fieldsets = [
            ("base",{'fields':['name','gender','age','password','is_valid']}),
            ]
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('pk', 'name')
 
# admin.site.register(User,UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # 列表页属性
    list_display = ['pk', 'title', 'author', 'publish_time']
    list_filter = ['title','author']
    search_fields = ['title','author']
    list_per_page = 5

    # 添加，修改页属性
    fieldsets = [
            ("base",{'fields':['title', 'author','content','tag', 'img_path','is_valid']}),
            ]
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('pk', 'title')
    

# admin.site.register(Post,PostAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    # 列表页属性    
    list_display = ['pk', 'user_id', 'text', 'time']
    list_filter = ['user_id']
    search_fields = ['user_id']
    list_per_page = 5

    # 添加，修改页属性
    fieldsets = [
            ("base",{'fields':['user_id', 'text']}),
            ]
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('pk',)