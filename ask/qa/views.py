from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator


def q_list(request):
    qs = Question.objects.all()
    # qs = qs.order_by('-id')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('q_list') + '?page='

    return render(request, 'list.html', {
        'title': Question.objects.title,
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def popular(request):
    qs = Question.objects.all()
    # qs = qs.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list_rating.html', {
        'title': Question.objects.title,
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    # form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
        # 'form': form,
    })

