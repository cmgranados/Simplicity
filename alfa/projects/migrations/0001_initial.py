# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('af_pr_project', (
            ('project_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_projecttype', to=orm['types_simplicity.Type'])),
            ('business_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_businesstype', to=orm['types_simplicity.Type'])),
            ('client_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_clienttype', to=orm['types_simplicity.Type'])),
            ('date_started', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('partaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'ProjectAssociation'
        db.create_table('af_pj_project_association', (
            ('association_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projectassociation_projectid', to=orm['projects.Project'])),
            ('association_project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projectassociation_associationproject', to=orm['projects.Project'])),
        ))
        db.send_create_signal(u'projects', ['ProjectAssociation'])

        # Adding unique constraint on 'ProjectAssociation', fields ['project_id', 'association_project']
        db.create_unique('af_pj_project_association', ['project_id_id', 'association_project_id'])

        # Adding model 'RequirementAssociation'
        db.create_table('af_pj_requirement_association', (
            ('association_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('requirement_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.Requirement'])),
        ))
        db.send_create_signal(u'projects', ['RequirementAssociation'])

        # Adding unique constraint on 'RequirementAssociation', fields ['project_id', 'requirement_id']
        db.create_unique('af_pj_requirement_association', ['project_id_id', 'requirement_id_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'RequirementAssociation', fields ['project_id', 'requirement_id']
        db.delete_unique('af_pj_requirement_association', ['project_id_id', 'requirement_id_id'])

        # Removing unique constraint on 'ProjectAssociation', fields ['project_id', 'association_project']
        db.delete_unique('af_pj_project_association', ['project_id_id', 'association_project_id'])

        # Deleting model 'Project'
        db.delete_table('af_pr_project')

        # Deleting model 'ProjectAssociation'
        db.delete_table('af_pj_project_association')

        # Deleting model 'RequirementAssociation'
        db.delete_table('af_pj_requirement_association')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project', 'db_table': "'af_pr_project'"},
            'business_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_businesstype'", 'to': u"orm['types_simplicity.Type']"}),
            'client_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_clienttype'", 'to': u"orm['types_simplicity.Type']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'date_started': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'partaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'project_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_projecttype'", 'to': u"orm['types_simplicity.Type']"})
        },
        u'projects.projectassociation': {
            'Meta': {'unique_together': "(('project_id', 'association_project'),)", 'object_name': 'ProjectAssociation', 'db_table': "'af_pj_project_association'"},
            'association_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'association_project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projectassociation_associationproject'", 'to': u"orm['projects.Project']"}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projectassociation_projectid'", 'to': u"orm['projects.Project']"})
        },
        u'projects.requirementassociation': {
            'Meta': {'unique_together': "(('project_id', 'requirement_id'),)", 'object_name': 'RequirementAssociation', 'db_table': "'af_pj_requirement_association'"},
            'association_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'requirement_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.Requirement']"})
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

    complete_apps = ['projects']