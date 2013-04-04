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
    
    in your postfix vhosts configuration:
    query = SELECT name FROM django_postfix_postfixdomain;
    
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
    
    in your postfix vmaps configuration:
    query = SELECT domain.name || '/' || mailbox.name || '/' \
            FROM django_postfix_postfixmailbox as mailbox, django_postfix_postfixdomain as domain  \
            WHERE mailbox.name='%u' AND domain.name='%d';
            
    """
    class Meta:
        verbose_name = _("Mailbox")
        verbose_name_plural = _("Mailboxes")
        
    name = models.CharField(max_length=512)
    domain = models.ForeignKey('PostfixDomain', related_name='mailboxes')
    
    # Anything else should be optional
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PostfixMailbox, self).save(force_insert, force_update) 
        
    def __unicode__(self):
        return '%s@%s'%(self.name, self.domain.name)
        
        
class PostfixUser(models.Model):
    """
        Manage postfix authorized senders
        
    """
    class Meta:
        verbose_name = _("Contributor")
        verbose_name_plural = _("Contributors")
    
    name = models.CharField(max_length=512)
    domain = models.ForeignKey('PostfixDomain', related_name='contributors')
    
    def __unicode__(self):
        return '%s@%s'%(self.name, self.domain.name)
        
        
        
        