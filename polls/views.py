from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views import generic
from django.utils import timezone
# from django.template import loader
from .models import Choice, Question
from django.urls import reverse


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
# def index(request):
#     """载入polls/index.html模板文件，并且向它传递一个上下文(context)"""
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
# def index(request):
#     """
#     快捷函数：render()
#     不需要导入loader 和 HttpResponse
#     载入模板，填充上下文，在返回由它生成的HttpResponse对象
#     """
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)
# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         """ 问题不存在，抛出一个Http404异常 """
# #         raise Http404("Question does not exist")
# #     return render(request, 'polls/detail.html', {'question': question})
#
# def detail(request, question_id):
#     """
#     获取对象：快捷函数如果不存在就抛出Http404错误
#     为什么我们使用辅助函数 get_object_or_404() 而不是自己捕获 ObjectDoesNotExist 异常呢？
#     还有，为什么模型 API 不直接抛出 ObjectDoesNotExist 而是抛出 Http404 呢？
#     因为这样做会增加模型层和视图层的耦合性。
#     指导 Django 设计的最重要的思想之一就是要保证松散耦合。
#     一些受控的耦合将会被包含在 django.shortcuts 模块中。
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
# # def vote(request, question_id):
# #     return HttpResponse("You're voting on question %s." % question_id)
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice."
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # """ Return the last five Published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        """
        Return the last five published question (not including those set to be
        published in the future.
        :return:
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any question that aren't published yet.
        :return:
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
