# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Requirement'
        db.create_table('kp_req_requirement', (
            ('requirement_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['types_simplicity.Type'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['states_simplicity.State'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('is_active', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'requirements', ['Requirement'])

        # Adding model 'RequirementBusinessRule'
        db.create_table('kp_req_requirement_business_rule', (
            ('requirement_business_rule_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
            ('business_rule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['businessrules.BusinessRule'])),
        ))
        db.send_create_signal(u'requirements', ['RequirementBusinessRule'])

        # Adding unique constraint on 'RequirementBusinessRule', fields ['requirement', 'business_rule']
        db.create_unique('kp_req_requirement_business_rule', ['requirement_id', 'business_rule_id'])

        # Adding model 'RequirementInput'
        db.create_table('kp_req_requirement_input', (
            ('requirement_input_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'requirements', ['RequirementInput'])

        # Adding model 'RequirementOutput'
        db.create_table('kp_req_requirement_output', (
            ('requirement_output_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'requirements', ['RequirementOutput'])

        # Adding model 'AcceptanceCriteria'
        db.create_table('kp_req_acceptance_criteria', (
            ('acceptance_criteria_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'requirements', ['AcceptanceCriteria'])


    def backwards(self, orm):
        # Removing unique constraint on 'RequirementBusinessRule', fields ['requirement', 'business_rule']
        db.delete_unique('kp_req_requirement_business_rule', ['requirement_id', 'business_rule_id'])

        # Deleting model 'Requirement'
        db.delete_table('kp_req_requirement')

        # Deleting model 'RequirementBusinessRule'
        db.delete_table('kp_req_requirement_business_rule')

        # Deleting model 'RequirementInput'
        db.delete_table('kp_req_requirement_input')

        # Deleting model 'RequirementOutput'
        db.delete_table('kp_req_requirement_output')

        # Deleting model 'AcceptanceCriteria'
        db.delete_table('kp_req_acceptance_criteria')


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
        u'requirements.acceptancecriteria': {
            'Meta': {'object_name': 'AcceptanceCriteria', 'db_table': "'kp_req_acceptance_criteria'"},
            'acceptance_criteria_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
        u'requirements.requirementbusinessrule': {
            'Meta': {'unique_together': "(('requirement', 'business_rule'),)", 'object_name': 'RequirementBusinessRule', 'db_table': "'kp_req_requirement_business_rule'"},
            'business_rule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['businessrules.BusinessRule']"}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.Requirement']"}),
            'requirement_business_rule_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'requirements.requirementinput': {
            'Meta': {'object_name': 'RequirementInput', 'db_table': "'kp_req_requirement_input'"},
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.Requirement']"}),
            'requirement_input_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'requirements.requirementoutput': {
            'Meta': {'object_name': 'RequirementOutput', 'db_table': "'kp_req_requirement_output'"},
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.Requirement']"}),
            'requirement_output_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
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

    complete_apps = ['requirements']