import pyes
import logviewer.views.metadata as metadata
from logviewer.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
'''
    Management page for filters.

    Filters can be created, edited and deleted.

    @package logviewer.views.managefilters
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

LOGVIEWER_SERVER = '127.0.0.1:9200'

@login_required(login_url='/login')
def manage(request):
    '''
        Returns log data between given date and now.

        @param request HTTP request object
        @returns Filter managament page
    '''
    #b = FilterOptions(filter_name = 'osman' )
    #b.save()

    filters = ''
    for f in Filter.objects.all():
        filters += '<option value="'+f.filter_name+'">'+f.filter_name+'</option>'

    return TemplateResponse(request, 'filtermanage.html', 
            context = {'filter_names': filters})
