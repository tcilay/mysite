from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']})
#     ]
"""
    包含“添加头片”的表单
    创建“投票”对象时直接添加n个选项
"""


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    """列表页中以列的形式展示这个对象"""
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    """
    展示的过滤器类型取决你你要过滤的字段的类型。
    因为 pub_date 是类 DateTimeField，Django 知道要提供哪个过滤器：“任意时间”，“今天”，“过去7天”，“这个月”和“今年”。
    """
    list_filter = ['pub_date']
    # 搜索条件
    search_fields = ['question_text']


# admin.sites.site.register(Choice)
admin.sites.site.register(Question, QuestionAdmin)
