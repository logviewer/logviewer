import pyes
import logviewer.views.metadata as metadata
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

'''
    Index page of LogViewer
    
    If user is authenticated redirects user to default log stream else asks for login credentials.

    @package logviewer.views.index
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''


@login_required(login_url='/login')
def index(request):
    '''
        Returns column names of given log type.

        @param request HTTP request object
        @returns login page or redirect to default log stream
    '''
    if not request.user.is_authenticated():
        return redirect('/login')

    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file()
    default_log = [x for x in metadata_dict if 'default' in metadata_dict[x] and metadata_dict[x]['default'].upper() == 'YES'][0]

    return redirect('/search/%s/' % default_log)
