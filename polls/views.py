# Create your views here.

from django.http import HttpResponse
from django.http import Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll


#def index(request):
#    #return HttpResponse("Hello, world. You're at the poll index.")
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    # output = ', '.join([p.question for p in latest_poll_list])
#    # template = loader.get_template('polls/index.html')
#    # context = RequestContext(request, {
#    #	'latest_poll_list': latest_poll_list,
#    #	})
#    #context = {'latest_poll_list': latest_poll_list}
#    # one way of doing it
#    #return HttpResponse(template.render(context))
#    return render(request, 'index.html', {'latest_poll_list': latest_poll_list})
#
#
#def detail(request, poll_id):
#    #try:
#    #	poll = Poll.objects.get(pk=poll.id)
#    #except Poll.DoesNotExist:
#    #	raise Http404
#    poll = get_object_or_404(Poll, pk=poll_id)
#
#    return render(request, 'detail.html', {'poll': poll})
#
#    # return HttpResponse("You're looking at poll %s" % poll_id)
#
#
#def results(request, poll_id):
#    poll = get_object_or_404(Poll, pk=poll_id)
#    return render(request, 'results.html', {'poll': poll})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form
        return render(request, 'detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice
        # if a user hist the BACK button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))




