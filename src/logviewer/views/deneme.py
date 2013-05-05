from django.http import HttpResponse
from haystack.query import SearchQuerySet
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def deneme(request):
        return render_to_response("deneme.html")
