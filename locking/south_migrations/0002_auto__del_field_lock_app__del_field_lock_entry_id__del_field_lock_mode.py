# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'Lock.app'
        db.delete_column('locking_lock', 'app')

        # Deleting field 'Lock.entry_id'
        db.delete_column('locking_lock', 'entry_id')

        # Deleting field 'Lock.model'
        db.delete_column('locking_lock', 'model')

        # Adding field 'Lock.object_id'
        db.add_column('locking_lock', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Lock.content_type'
        db.add_column('locking_lock', 'content_type', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['contenttypes.ContentType']), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Adding field 'Lock.app'
        db.add_column('locking_lock', 'app', self.gf('django.db.models.fields.CharField')(max_length=255, null=True), keep_default=False)

        # Adding field 'Lock.entry_id'
        db.add_column('locking_lock', 'entry_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=-1, db_index=True), keep_default=False)

        # Adding field 'Lock.model'
        db.add_column('locking_lock', 'model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True), keep_default=False)

        # Deleting field 'Lock.object_id'
        db.delete_column('locking_lock', 'object_id')

        # Deleting field 'Lock.content_type'
        db.delete_column('locking_lock', 'content_type_id')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 23, 14, 21, 4, 303732)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 23, 14, 21, 4, 303516)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'locking.lock': {
            'Meta': {'object_name': 'Lock'},
            '_hard_lock': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'hard_lock'", 'blank': 'True'}),
            '_locked_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'locked_at'"}),
            '_locked_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'working_on_locking_lock'", 'null': 'True', 'db_column': "'locked_by'", 'to': "orm['auth.User']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }
    
    complete_apps = ['locking']
