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
    filter_forms = ''
    for f in Filter.objects.all():
        filters += '<option value="'+f.filter_name+'">'+f.filter_name+'</option>'
        filter_forms += '<div id="' + f.filter_name + '" style="display:none" >'
        filter_forms += '<table><tr>'
        for ff in FilterOptions.objects.filter(filter_name = f.filter_name).values():
            filter_forms += '<td><b><center>'+ str(ff['column']) +\
                            '</center></b><br> <input value="' +\
                            str(ff['regex']) + '" onchange="editfilterget(\''+\
                            str(ff['column']) +'\', this.value);"'+' type="text" name="'+\
                            str(ff['column']) + '" id="'+str(ff['column'])+'"></td>'
        filter_forms += '</tr></table>'
        #filter_forms += '<button class="btn btn-primary" '+\
        #        'onclick="editfilterget();" type="button" '+\
        #        'value="Save">Save</button></div>'
        filter_forms += '</div>'
    return TemplateResponse(request, 'filtermanage.html', 
            context = {'filter_names': filters, 'filter_forms': filter_forms})

def deletefilter(request):
    if request.method == 'GET':
        response = HttpResponse()
        fname = request.GET['filter_name']
        try:
            FilterOptions.objects.filter(filter_name = fname).delete()
            Filter.objects.filter(filter_name = fname).delete()
            response.write('Deleted')
        except:
            response.write('Error! Filter could not deleted from database.')
        return response

def editfilter(request):
    if request.method == 'GET':
        response = HttpResponse()
        fname = request.GET['filter_name']
        reg = request.GET['regex']
        cl = request.GET['column_name']
        try:
            FilterOptions.objects.filter(filter_name = fname, 
                                         column = cl).update(regex = reg)
            response.write('Saved')
        except:
            response.write('Error! ')
        
        return response

def savefilter(request):
    if request.method == 'GET':
        response = HttpResponse()
        fname = request.GET['filter_name']
        finfo = request.GET['filter_info']
        try:
            Filter.objects.create(filter_name=fname)
            for row in finfo.split(';'):
                cl = row.split(',')[0]
                reg = row.split(',')[1]
                p = FilterOptions(filter_name_id = fname,
                                            column = cl,
                                            regex = reg)
                p.save()
            
            response.write('Saved')
        except Exception,e:
            response.write('Error! '+ str(e))

        return response

def getfilters(request):
    if request.method == 'GET':
        response = HttpResponse()
        try:
            out = '<select id="filterdropdown" style="width:auto;">'
            for f in Filter.objects.all():
                out += '<option value="' + f.filter_name + '">' + f.filter_name + '</option>'
            out += '</select>'
            response.write(out)
        except:
            response.write('Error! ')

        return response


def getfilterinfo(request):
    if request.method == 'GET':
        response = HttpResponse()
        fname = request.GET['filter_name']
        try:
            out = ''
            for ff in FilterOptions.objects.filter(filter_name = fname).values():
                out += str(ff['column']) +','+ str(ff['regex']) + ';'
            
            response.write(out[:-1])
        except:
            response.write('Error! ')

        return response






