# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PostfixUser.status'
        db.add_column(u'django_postfix_postfixuser', 'status',
                      self.gf('django.db.models.fields.CharField')(default='OK', max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PostfixUser.status'
        db.delete_column(u'django_postfix_postfixuser', 'status')


    models = {
        u'django_postfix.postfixdomain': {
            'Meta': {'object_name': 'PostfixDomain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'django_postfix.postfixmailbox': {
            'Meta': {'object_name': 'PostfixMailbox'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mailboxes'", 'to': u"orm['django_postfix.PostfixDomain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'django_postfix.postfixuser': {
            'Meta': {'object_name': 'PostfixUser'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contributors'", 'to': u"orm['django_postfix.PostfixDomain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'OK'", 'max_length': '6'})
        }
    }

    complete_apps = ['django_postfix']