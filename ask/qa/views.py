from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from qa.models import Question
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, questions):
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

    paginator = Paginator(questions, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator


def q_list(request):
    questions = Question.objects.all()
    questions = questions.order_by('-id')
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('q_list') + '?page='

    return render(request, 'list.html', {
        # 'title': 'Latest',
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def popular(request):
    questions = Question.objects.all()
    questions = questions.order_by('-rating')
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list.html', {
        # 'title': 'Popular',
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': question.pk})
    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def question_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            # form._user = request.user
            ask = form.save()
            url = reverse('question_detail', args=[ask.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask.html', {
        'form': form
    })


def question_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form._user = request.user
            answer = form.save()
            url = reverse('question_detail', args=[answer.question.id])
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')

