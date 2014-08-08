# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Precondition'
        db.create_table('kp_pco_precondition', (
            ('precondition_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
        ))
        db.send_create_signal(u'preconditions', ['Precondition'])

        # Adding model 'PreconditionRequirement'
        db.create_table('kp_pco_precondition_requirement', (
            ('precondition_requirement_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
            ('precondition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['preconditions.Precondition'])),
        ))
        db.send_create_signal(u'preconditions', ['PreconditionRequirement'])

        # Adding unique constraint on 'PreconditionRequirement', fields ['requirement', 'precondition']
        db.create_unique('kp_pco_precondition_requirement', ['requirement_id', 'precondition_id'])

        # Adding model 'PreconditionDescription'
        db.create_table('kp_pco_precondition_description', (
            ('precondition_description_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('precondition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['preconditions.Precondition'])),
        ))
        db.send_create_signal(u'preconditions', ['PreconditionDescription'])


    def backwards(self, orm):
        # Removing unique constraint on 'PreconditionRequirement', fields ['requirement', 'precondition']
        db.delete_unique('kp_pco_precondition_requirement', ['requirement_id', 'precondition_id'])

        # Deleting model 'Precondition'
        db.delete_table('kp_pco_precondition')

        # Deleting model 'PreconditionRequirement'
        db.delete_table('kp_pco_precondition_requirement')

        # Deleting model 'PreconditionDescription'
        db.delete_table('kp_pco_precondition_description')


    models = {
        u'preconditions.precondition': {
            'Meta': {'object_name': 'Precondition', 'db_table': "'kp_pco_precondition'"},
            'precondition_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.Requirement']"})
        },
        u'preconditions.preconditiondescription': {
            'Meta': {'object_name': 'PreconditionDescription', 'db_table': "'kp_pco_precondition_description'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'precondition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['preconditions.Precondition']"}),
            'precondition_description_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'preconditions.preconditionrequirement': {
            'Meta': {'unique_together': "(('requirement', 'precondition'),)", 'object_name': 'PreconditionRequirement', 'db_table': "'kp_pco_precondition_requirement'"},
            'precondition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['preconditions.Precondition']"}),
            'precondition_requirement_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.Requirement']"})
        },
        u'requirements.requirement': {
            'Meta': {'object_name': 'Requirement', 'db_table': "'kp_req_requirement'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'requirement_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['states_simplicity.State']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
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

    complete_apps = ['preconditions']