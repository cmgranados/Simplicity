# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StateType'
        db.create_table('adm_state_type', (
            ('state_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'states_simplicity', ['StateType'])

        # Adding model 'State'
        db.create_table('adm_state', (
            ('state_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('state_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['states_simplicity.StateType'])),
        ))
        db.send_create_signal(u'states_simplicity', ['State'])


    def backwards(self, orm):
        # Deleting model 'StateType'
        db.delete_table('adm_state_type')

        # Deleting model 'State'
        db.delete_table('adm_state')


    models = {
        u'states_simplicity.state': {
            'Meta': {'object_name': 'State', 'db_table': "'adm_state'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['states_simplicity.StateType']"})
        },
        u'states_simplicity.statetype': {
            'Meta': {'object_name': 'StateType', 'db_table': "'adm_state_type'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['states_simplicity']