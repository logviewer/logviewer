import os
import re
import json
from django.core.serializers.json import DjangoJSONEncoder
import logviewer.views.metadata as metadata
from logviewer.logviewer_settings import LOGVIEWER_SERVER
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
'''
    Management page for settings.

    Choose showed log columns, choose log column delimiter, edit
    elasticsearch server ip

    @package logviewer.views.settings
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''
LOGVIEWER_SETTINGS = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logviewer_settings.py')
@login_required(login_url='/login')
def settings(request):
    '''
        Settings main page

        @param request HTTP request object
        @returns Settings page
    '''
    return_dict = {}
    return_dict['ip'] = LOGVIEWER_SERVER

    return TemplateResponse(request, 'settings.html', context=return_dict)

@login_required(login_url='/login')
def save_server(request):
    '''
        Save server settings

        @param request HTTP request object
        @returns Settings page
    '''
    ip = request.GET.get('ip')

    if not re.match('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,5}$', ip):
        return HttpResponse(json.dumps({'error' : 'Not a valid IP:Port couple.'}, cls=DjangoJSONEncoder), mimetype="application/json")

    try:
        with open(LOGVIEWER_SETTINGS, "r") as sources:
            lines = sources.readlines()
    
        with open(LOGVIEWER_SETTINGS, "w") as sources:
            for line in lines:
                sources.write(re.sub(r'^LOGVIEWER_SERVER.*', 'LOGVIEWER_SERVER = \'%s\'' % (ip), line))
    except:
        return HttpResponse(json.dumps({'error' : 'Cannot save IP.'}, cls=DjangoJSONEncoder), mimetype="application/json")

    return HttpResponse(json.dumps({'success' : 'Saved IP successfully.'}, cls=DjangoJSONEncoder), mimetype="application/json")

@login_required(login_url='/login')
def get_log_settings(request):
    '''
        Get log settings

        @param request HTTP request object
        @returns Settings page
    '''
    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file()

    log_type = request.GET.get('log_type')

    return_json = {}
    return_json['default'] = metadata_dict[log_type]['default']
    return_json['delimiter'] = metadata_dict[log_type]['delimiter'].replace("'","")
    return_json['shown_columns'] = metadata_dict[log_type]['shown_columns'].split(',')
    return_json['filter_columns'] = metadata_dict[log_type]['filter_columns']

    return HttpResponse(json.dumps(return_json, cls=DjangoJSONEncoder), mimetype="application/json")

@login_required(login_url='/login')
def get_log_types(request):
    '''
        Get log types

        @param request HTTP request object
        @returns Settings page
    '''
    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file()

    return_json = {}
    return_json['log_types'] = metadata_dict.keys()

    return HttpResponse(json.dumps(return_json, cls=DjangoJSONEncoder), mimetype="application/json")

@login_required(login_url='/login')
def save_log_settings(request):
    '''
        Write log options

        @returns Settings page
    '''
    log_type = request.GET.get('log_type')
    default = request.GET.get('default')
    delimiter = request.GET.get('delimiter')
    filter_columns = request.GET.get('filter_columns')
    shown_columns = request.GET.get('shown_columns')

    mdata = metadata.MetaData()
    if mdata.write_ini_file(log_type, {'default': default, 
                                       'filter_columns': filter_columns,
                                       'shown_columns': shown_columns,
                                       'delimiter': delimiter}):
        return HttpResponse(json.dumps({'success' : 'Successfully saved configuration.'}, cls=DjangoJSONEncoder), mimetype="application/json")

    return HttpResponse(json.dumps({'error' : 'Cannot save configuration.'}, cls=DjangoJSONEncoder), mimetype="application/json")
