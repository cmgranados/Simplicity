# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BusinessRule'
        db.create_table('kp_br_business_rule', (
            ('business_rule_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['types_simplicity.Type'])),
            ('state_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['states_simplicity.State'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'businessrules', ['BusinessRule'])


    def backwards(self, orm):
        # Deleting model 'BusinessRule'
        db.delete_table('kp_br_business_rule')


    models = {
        u'businessrules.businessrule': {
            'Meta': {'object_name': 'BusinessRule', 'db_table': "'kp_br_business_rule'"},
            'business_rule_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'state_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['states_simplicity.State']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['types_simplicity.Type']"})
        },
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
        },
        u'types_simplicity.type': {
            'Meta': {'object_name': 'Type', 'db_table': "'adm_type'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_type_id'", 'to': u"orm['types_simplicity.Type']"}),
            'type_classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['types_simplicity.TypeClassification']"}),
            'type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'types_simplicity.typeclassification': {
            'Meta': {'object_name': 'TypeClassification', 'db_table': "'adm_type_classification'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type_classification_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['businessrules']