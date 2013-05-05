import logviewer.views.metadata as metadata
from django import template
'''
    Template tag for log streams.

    This template tag creates log stream dropdown list dynamically.

    @package logviewer.templatetags.metadata_tags
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

register = template.Library()

@register.simple_tag
def show_metadata():
    '''
        Returns log stream list to be used in dropdown menu

        @returns HTTP response which includes log stream list as link list
    '''
    mdata = metadata.MetaData()
    metadata_dict = mdata.read_ini_file().keys()
    retHtml = ''
    for m_key in metadata_dict:
        retHtml += '<li><a href="/search/%s">%s</a></li>' % (m_key, m_key.upper())

    return retHtml
