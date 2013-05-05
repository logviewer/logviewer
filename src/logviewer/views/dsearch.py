import re
import pyes
import json
import datetime
import logviewer.views.metadata as metadata
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
'''
    Dynamic search module.

    Makes search according to GET request and then returns elasticsearch result as JSON.

    @package logviewer.views.dsearch
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

LOGVIEWER_SERVER = '127.0.0.1:9500'

@login_required(login_url='/login')
def dsearch(request, log_type, log_date):
    '''
        Returns log data between given date and now.

        @param request HTTP request object
        @param log_type String: GET request parameter which holds log type of which data will be returned
        @param log_date String: The date of first log we want in our JSON.
        @returns HTTP response which includes log data in JSON format.
    '''

    return_json = {}
    return_json['aaData'] = []

    # Show parameters
    iDisplayLength = request.GET.get('iDisplayLength')
    iDisplayStart = request.GET.get('iDisplayStart')
    sort_direction = request.GET.get('sSortDir_0')

    # Set sEcho
    sEcho = request.GET.get('sEcho')
    return_json['sEcho'] = sEcho if sEcho else 1

    conn = pyes.ES(LOGVIEWER_SERVER)

    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file()
    return_json['sColumns'] = metadata_dict[log_type]['shown_columns'].split(',')

    i = 0
    qs = []
    while True:
        q = request.GET.get('sSearch_' + str(i))
        if q == None:
            break

        if q != '':
            q = pyes.WildcardQuery(return_json['sColumns'][i],q)
            qs.append(q)

        i += 1

    q = pyes.RangeQuery(qrange=pyes.ESRange('logdate'))
    qs.append(q)

    s = pyes.BoolQuery(must=qs)

    log_type = log_type.lower()
    if log_type not in metadata_dict:
        return HttpResponse(json.dumps('There is no log type as %s' % log_type), mimetype="application/json")

    search_result = conn.search(query=s,
                           indices=['logviewer'],
                           doc_types=[log_type],
                           sort='logdate:' + sort_direction,
                           start=iDisplayStart,
                           size=int(iDisplayLength))

    return_json['iTotalRecords'] = search_result.count()
    return_json['iTotalDisplayRecords'] = search_result.count()

    try:
        for log in search_result:
            values = []
            for column in return_json['sColumns']:
                if column == 'logdate':
                    values.append(re.sub('^([0-9]{4})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})$',
                                         '\g<1>/\g<2>/\g<3> \g<4>:\g<5>:\g<6>',
                                         log[column]))
                    continue
                values.append(log[column])
    
            return_json['aaData'].append(values)
    except TypeError:
        pass

    return HttpResponse(json.dumps(return_json, cls=DjangoJSONEncoder), mimetype="application/json")
    #conn = pyes.ES(LOGVIEWER_SERVER)

    #mdata = metadata.MetaData()
    #metadata_dict = mdata.read_ini_file()

    #s = pyes.RangeQuery(qrange=pyes.ESRange('logdate'))

    #log_type = log_type.lower()
    #if log_type not in metadata_dict:
    #    return HttpResponse(json.dumps('There is no log type as %s' % log_type), mimetype="application/json")

    #return_json = {}
    #return_json['column'] = metadata_dict[log_type]['shown_columns'].split(',')
    #return_json['data'] = []

    #for log in conn.search(query=s,
    #                       indices=['logviewer'],
    #                       doc_types=[log_type],
    #                       sort='logdate:desc',
    #                       size=int(metadata_dict[log_type]['log_count'])):
    #    return_json['data'].append(log)

    #return HttpResponse(json.dumps(return_json, cls=DjangoJSONEncoder), mimetype="application/json")

@login_required(login_url='/login')
def dsearch_columns(request, log_type):
    '''
        Returns column names of given log type.

        @param request HTTP request object
        @param log_type String: GET request parameter which holds log type of which log data will be returned
        @returns HTTP response which includes log type's columns in JSON format.
    '''
    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file()

    return_json = metadata_dict[log_type]['shown_columns'].split(',')

    return HttpResponse(json.dumps(return_json, cls=DjangoJSONEncoder), mimetype="application/json")
