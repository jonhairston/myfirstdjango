# Create your views here.

from django.http import HttpResponse
from django.http import Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# import the models to the views page
from polls.models import Choice, Poll


# Drew wants these as functional views because of the awesomeness provided

# What do you need to display these views properly? Ask yourself this question first

# What does the view need to work? It is always the request from the user, and in the
# detail pages the id of what ever item that was clicked on

# What does render need to draw correctly? That would be the parameters in render
# render needs the request first, the template second, and the context instance dictionary,
# which is a dictionary of values to add to the template context, which is usually defined in the
# view itself
def index(request):

    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'index.html', {'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'results.html', {'poll': poll})


def vote(request, poll_id):

    # needs object to search and the search parameters
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        # if you get the vote post it to the db
        selected_choice = p.choices.get(pk=request.POST['choice'])
   # else post a 404 error
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form
        return render(request, 'detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }
        )
    else:
        # else go to the next page and show the vote count
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice
        # if a user hist the BACK button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))







