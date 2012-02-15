# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ZipCode'
        db.create_table(u'zip_codes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('general', ['ZipCode'])


    def backwards(self, orm):
        
        # Deleting model 'ZipCode'
        db.delete_table(u'zip_codes')


    models = {
        'general.zipcode': {
            'Meta': {'object_name': 'ZipCode', 'db_table': "u'zip_codes'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['general']
