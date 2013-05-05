import pyes
import logviewer.views.metadata as metadata
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
'''
    Static search module.

    Returns table to be filled with logs later.

    @package logviewer.views.search
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

LOGVIEWER_SERVER = '127.0.0.1:9200'

@login_required(login_url='/login')
def search(request, log_type):
    '''
        Creates table according to log type and its columns.

        @param request HTTP request object
        @param log_type String: GET request parameter which holds log type of which data will be returned
        @returns index.html template with table in it.
    '''
    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file()

    fields = metadata_dict[log_type]['shown_columns']

    return_html = '<table id="example" class="display" style="table-layout:fixed">'
    return_html += '<thead>'
    return_html += '<tr>'

    for field in fields.split(','):
        return_html += '<th>' + field.upper() + '</th>'

    return_html += '</tr>'
    return_html += '</thead>'


    return_html += '</table>'
    return TemplateResponse(request, 'index.html', context={'table': return_html})
