# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostfixDomain'
        db.create_table(u'django_postfix_postfixdomain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'django_postfix', ['PostfixDomain'])

        # Adding model 'PostfixMailbox'
        db.create_table(u'django_postfix_postfixmailbox', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mailboxes', to=orm['django_postfix.PostfixDomain'])),
        ))
        db.send_create_signal(u'django_postfix', ['PostfixMailbox'])

        # Adding model 'PostfixUser'
        db.create_table(u'django_postfix_postfixuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contributors', to=orm['django_postfix.PostfixDomain'])),
        ))
        db.send_create_signal(u'django_postfix', ['PostfixUser'])


    def backwards(self, orm):
        # Deleting model 'PostfixDomain'
        db.delete_table(u'django_postfix_postfixdomain')

        # Deleting model 'PostfixMailbox'
        db.delete_table(u'django_postfix_postfixmailbox')

        # Deleting model 'PostfixUser'
        db.delete_table(u'django_postfix_postfixuser')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['django_postfix']