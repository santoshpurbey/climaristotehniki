from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .models import Project, Category


def home(request):
    output = _("Welcome to my site.")
    return render(request, 'home.html', {'output': output})


def about(request):
    return render(request, 'about.html', {})



def contact(request):
    return render(request, 'contact.html', {})


def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})


def portfolio_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'project': project})


# redirect to 404

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
