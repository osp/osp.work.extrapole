# -*- coding: utf-8 -*-
"""
 
 django_maildir.views
 
"""

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from django_maildir.models import *

def index(request):
    data = {}
    data['messages'] = Message().get_all()
    return render_to_response("maildir_index.html", data, context_instance = RequestContext(request))
    
def get(request, mailbox, mailbox_key):
    pass
    
def filter(request, key, values):
    pass

    