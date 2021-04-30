from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-pk')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default="", max_length=255)
    text = models.TextField(default="")
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author", on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="question_like_user", blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})
        # return '/question/' + str(self.id) + '/'


class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('added_at',)

    def __str__(self):
        return 'Answer by {}'.format(self.author)



