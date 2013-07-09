# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('hello_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hello', ['Person'])

        # Adding model 'ReqData'
        db.create_table('hello_reqdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('get', self.gf('django.db.models.fields.TextField')()),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('cookies', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hello', ['ReqData'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('hello_person')

        # Deleting model 'ReqData'
        db.delete_table('hello_reqdata')


    models = {
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