# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Carosel.description'
        db.delete_column('carosel_carosel', 'description')

        # Deleting field 'Carosel.title'
        db.delete_column('carosel_carosel', 'title')

        # Deleting field 'Carosel.slug'
        db.delete_column('carosel_carosel', 'slug')

        # Deleting field 'Carosel.id'
        db.delete_column('carosel_carosel', 'id')

        # Adding field 'Carosel.page_ptr'
        db.add_column('carosel_carosel', 'page_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2012, 8, 23, 0, 0), to=orm['pages.Page'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'Carosel.carosel'
        db.add_column('carosel_carosel', 'carosel',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 8, 23, 0, 0), max_length=50),
                      keep_default=False)

        # Removing M2M table for field pages on 'Carosel'
        db.delete_table('carosel_carosel_pages')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Carosel.description'
        raise RuntimeError("Cannot reverse this migration. 'Carosel.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Carosel.title'
        raise RuntimeError("Cannot reverse this migration. 'Carosel.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Carosel.slug'
        raise RuntimeError("Cannot reverse this migration. 'Carosel.slug' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Carosel.id'
        raise RuntimeError("Cannot reverse this migration. 'Carosel.id' and its values cannot be restored.")
        # Deleting field 'Carosel.page_ptr'
        db.delete_column('carosel_carosel', 'page_ptr_id')

        # Deleting field 'Carosel.carosel'
        db.delete_column('carosel_carosel', 'carosel')

        # Adding M2M table for field pages on 'Carosel'
        db.create_table('carosel_carosel_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('carosel', models.ForeignKey(orm['carosel.carosel'], null=False)),
            ('page', models.ForeignKey(orm['pages.page'], null=False))
        ))
        db.create_unique('carosel_carosel_pages', ['carosel_id', 'page_id'])


    models = {
        'carosel.carosel': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Carosel', '_ormbases': ['pages.Page']},
            'carosel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        'carosel.caroselimage': {
            'Meta': {'object_name': 'CaroselImage'},
            'carosels': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['carosel.Carosel']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': "orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '[1, 2, 3]', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': "orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carosel']