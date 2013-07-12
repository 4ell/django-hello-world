# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table('hello_action', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('hello', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table('hello_action')


    models = {
        'hello.action': {
            'Meta': {'object_name': 'Action'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'contacts': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'hello.reqdata': {
            'Meta': {'object_name': 'ReqData'},
            'cookies': ('django.db.models.fields.TextField', [], {}),
            'get': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']