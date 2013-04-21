# -*- coding: utf-8 -*-
"""
 
 django_postfix.admin
 
"""

from django.contrib import admin

from django_postfix.models import *



class PostfixDomainAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    
class PostfixMailboxAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')
    list_filter = ('domain',)
    search_fields = ['name',]
    fieldsets = [
            (None, {'fields':('name','domain',)}),
            ]
            
class PostfixUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')
    list_filter = ('domain',)
    search_fields = ['name',]
    fieldsets = [
            (None, {'fields':(('name','domain'),'status')}),
            ]
    

    
admin.site.register(PostfixDomain, PostfixDomainAdmin)
admin.site.register(PostfixMailbox, PostfixMailboxAdmin)
admin.site.register(PostfixUser, PostfixUserAdmin)