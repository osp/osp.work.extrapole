# -*- coding: utf-8 -*-
"""
 
 django_maildir.models

 read-only models to access Maildirs
 It assumes postfix virtual domains configuration
 
 settings must have POSTFIX_VIRTUAL_MAILBOX_BASE
"""

import os
from mailbox import Maildir, MaildirMessage

import logging
logger = logging.getLogger(__name__)

from django_postfix.models import PostfixMailbox
from settings import POSTFIX_VIRTUAL_MAILBOX_BASE


class Message(object):
    """
    present a model for a message, everything in ther :)
    """
    
    def __init__(self):
        self.maildirs = {}
        
        mailboxes = PostfixMailbox.objects.all()
        for mb in mailboxes:
            try:
                mb_path = os.path.join(POSTFIX_VIRTUAL_MAILBOX_BASE, mb.domain.name, mb.name)
                print 'Try to MD: %s'%mb_path
                if mb.domain.name not in self.maildirs:
                    self.maildirs[mb.domain.name] = {}
                self.maildirs[mb.domain.name][mb.name] = Maildir(mb_path, factory=None, create=False)
            except Exception as e:
                logger.error(e)
                
    def message_prepare(self, message):
        ret = {}
        subject_list = message.get('Subject', 'No Subject').split('#')
        ret['subject'] = subject_list.pop(0)
        ret['tags'] = []
        for t in subject_list:
            ret['tags'].append(t)
        ret['body'] = message.get_payload()
        return ret 
        
                
    def get_all(self):
        ret = []
        for domain in self.maildirs:
            for mailbox in self.maildirs[domain]:
                md = self.maildirs[domain][mailbox]
                for (k,m) in md.iteritems():
                    mp = self.message_prepare(m)
                    mp['mailbox'] = '%s@%s'%(mailbox, domain)
                    mp['key'] = k
                    ret.append(mp)
                    
        return ret
        
    
        
    
    





