# -*- coding: utf-8 -*-
"""
 
 django_maildir.views
 
"""

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from django_maildir.models import *

import json

def index(request):
    #data = {}
    data = Message().get_all()
    for d in data:
        try:
            json.dumps(d)
        except Exception:
            print d
    return HttpResponse(json.dumps(data,indent=4, separators=(',', ': ')), mimetype="application/json")
    
def get_file(req, mailbox, key, filename):
    m = Message()
    f = m.get_file(mailbox,key,filename)
    return HttpResponse(f['data'], mimetype=f['mimetype'])
    

def get(request, mailbox, mailbox_key):
    pass
    
def filter(request, key, values):
    pass

    