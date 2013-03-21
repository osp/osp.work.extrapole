# -*- coding: utf-8 -*-
"""
 
 django_postfix.models
 
"""

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class PostfixDomain(models.Model):
    """
    Manage postfix virtual domains
    """
    class Meta:
        verbose_name = _("Domain")
        verbose_name_plural = _("Domains")
        
    name = models.CharField(max_length=512)
    
    # Anything else should be optional
    
    def __unicode__(self):
        return self.name

class PostfixMailbox(models.Model):
    """
    Manage postfix virtual mailboxes
    """
    class Meta:
        verbose_name = _("Mailbox")
        verbose_name_plural = _("Mailboxes")
        
    name = models.CharField(max_length=512)
    domain = models.ForeignKey('PostfixDomain', related_name='mailboxes')
    
    # Anything else should be optional
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(force_insert, force_update) 
        
    def __unicode__(self):
        return '%s@%s'%(self.name, self.domain.name)