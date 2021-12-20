from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.forms import formset_factory
from django.utils import timezone
from django.urls import reverse

from polls.models import Answer, Poll

from .forms import CreatePollForm, AnswerForm

class CreatePollView(CreateView):
    template_name = 'createPoll.html'
    context = {
        'poll_form': CreatePollForm,
        'answer_formset': formset_factory(AnswerForm, extra=3),
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        poll_form = self.context['poll_form'](request.POST)
        answer_formset = self.context['answer_formset'](request.POST)
        print(request.POST)
        print(poll_form)
        if poll_form.is_valid() and answer_formset.is_valid():
            poll = poll_form.save()
            for answer in answer_formset:
                Answer(
                    answer = answer.clean()['answer'],
                    question_id= Poll.objects.get(id=poll.id)
                ).save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name) 

class ResultsView(DetailView):
    Model = Poll
    template_name = "results.html"

    queryset = Poll.objects.all()

class VoteView(DetailView):
    Model = Poll
    template_name = "vote.html"
    queryset = Poll.objects.all()

    def post(self, request, *args, **kwargs):
        for key in request.POST:
            if key != 'csrfmiddlewaretoken':
                selected_answer = Answer.objects.get(pk=int(key))
                selected_answer.count += 1
                selected_answer.save()
        return HttpResponseRedirect(reverse('results', args=(kwargs['pk'],)))

class PollsView(ListView):
    Model = Poll
    template_name = "polls.html"
    queryset = Poll.objects.all()
