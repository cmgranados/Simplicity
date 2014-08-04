# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TypeClassification'
        db.create_table('adm_type_classification', (
            ('type_classification_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'types_simplicity', ['TypeClassification'])

        # Adding model 'Type'
        db.create_table('adm_type', (
            ('type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('type_classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['types_simplicity.TypeClassification'])),
            ('parent_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_type_id', to=orm['types_simplicity.Type'])),
        ))
        db.send_create_signal(u'types_simplicity', ['Type'])


    def backwards(self, orm):
        # Deleting model 'TypeClassification'
        db.delete_table('adm_type_classification')

        # Deleting model 'Type'
        db.delete_table('adm_type')


    models = {
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

    complete_apps = ['types_simplicity']