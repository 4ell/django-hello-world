# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReqData.priority'
        db.add_column('hello_reqdata', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReqData.priority'
        db.delete_column('hello_reqdata', 'priority')


    models = {
        'hello.action': {
            'Meta': {'object_name': 'Action'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
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
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']