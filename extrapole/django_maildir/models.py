# -*- coding: utf-8 -*-
"""
 
 django_maildir.models

 read-only models to access Maildirs
 It assumes postfix virtual domains configuration
 
 settings must have POSTFIX_VIRTUAL_MAILBOX_BASE
"""

import os
from mailbox import Maildir, MaildirMessage
from email.header import decode_header
import codecs

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
        self.codecs = {}
        
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
                
                
    def mail_decode(self, text, charset):
        if charset is None:
            charset = 'us-ascii'
        if charset not in self.codecs:
            self.codecs[charset] = codecs.getdecoder(charset)
        u, c = self.codecs[charset](text)
        return u
        
    def parse_subject(self, message, response):
        raw_subject = decode_header(message.get('Subject', 'No Subject'))
        subject_parts = []
        for decoded_string, charset in raw_subject:
            subject_parts.append(self.mail_decode(decoded_string, charset))
        subject = u' '.join(subject_parts)
        subject_list = subject.split('#')
        response['subject'] = subject_list.pop(0)
        response['tags'] = []
        for t in subject_list:
            response['tags'].append(t.strip())
            
    def parse_body(self, message, response):
        response['body'] = []
        for part in message.walk():
            T = part.get_content_maintype()
            if T == 'multipart':
                continue
            elif T == 'text':
                charset = part.get_charsets()[0]
                text = part.get_payload(decode=True)
                response['body'].append({'type':part.get_content_type(), 'payload':self.mail_decode(text, charset)})
            else:
                response['body'].append({'type':part.get_content_type(), 'payload': part.get_filename()})
    
    def message_prepare(self, message):
        ret = {}
        parts = ['subject', 'body']
        for part in parts:
            getattr(self, '_'.join(['parse',part]))(message, ret)
        return ret 
        
    def get_file(self, mailbox, key, filename):
        mb, domain = list(mailbox.split('@'))
        md = self.maildirs[domain][mb]
        message = md.get(key)
        for part in message.walk():
            if filename == part.get_filename():
                return {'mimetype':part.get_content_type(), 'data':part.get_payload(decode=True)}
                
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
        
    
        
    
    





