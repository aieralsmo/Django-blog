import re

from bs4 import BeautifulSoup
from django import template
register = template.Library()


@register.filter()
def prettify(raw=None, expect=None):
    
    if (expect is None) or (raw is None):

        return "Bad Request!"

    # 自己的文章用不着做处理，直接返回
    pretty = raw

    # 从其他网站上怕的文章 ，带有html标签，如果有html标签则说明是爬的文章，就需要提取文本
    if re.match(r"^<+.{0,}", raw): 
        soup = BeautifulSoup(raw, "html.parser")
        pretty = "点进去看就知道啦！"
        if len(soup.select(expect))>3:
            pretty = soup.select(expect)[0].text + soup.select(expect)[1].text + soup.select(expect)[2].text
    return pretty

@register.filter()
def datetimeformat(value, format='%Y-%m-%d'):
    return value.strftime(format)


@register.filter()
def tags_split(value, by=','):

    tags = [
        tag for tag in value.replace(' ', ',').split(by)
            if not( 
                tag == '评论' 
                or tag =='' 
                or tag.isdigit()
                )
    ]
    return tags


@register.filter()
def length(var):
    return len(var)



# @register.filter()
# def soup(var):
#     soup = BeautifulSoup(var, "html.parser")
    
#     div_crayon_syntax = soup.select('.crayon-syntax')

#     if div_crayon_syntax is None:
#         return False
#     ls = []
#     for idx in range(0,len(div_crayon_syntax)):
#         d=div_crayon_syntax[idx].extract()

#         l = len(d.select('.crayon-plain-wrap'))
#         for x in range(0, l):
#             x = d.textarea.text
#             # print(d)
#             ls.append(x)
#     return ls