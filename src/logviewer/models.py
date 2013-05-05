from django.db import models
from django.contrib.auth.models import User

'''
    Module that keeps database definitions. 

    @package logviewer.models
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

class Filter(models.Model):
    '''
        Parent class of all filter classes
    '''
    filter_name = models.CharField(max_length = 50, primary_key = True)
    
class FilterOptions(Filter):
    '''
        This filter allows users to write regular expression filters
    '''
    column = models.CharField(max_length = 50, null = False)
    regex = models.CharField(max_length = 50, null = False)



