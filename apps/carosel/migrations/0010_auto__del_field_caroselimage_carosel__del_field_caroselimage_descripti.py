# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CaroselImage.carosel'
        db.delete_column('carosel_caroselimage', 'carosel_id')

        # Deleting field 'CaroselImage.description'
        db.delete_column('carosel_caroselimage', 'description')

        # Deleting field 'CaroselImage.title'
        db.delete_column('carosel_caroselimage', 'title')

        # Deleting field 'CaroselImage.slug'
        db.delete_column('carosel_caroselimage', 'slug')

        # Adding field 'Carosel.caroselimages'
        db.add_column('carosel_carosel', 'caroselimages',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='default', to=orm['carosel.CaroselImage']),
                      keep_default=False)


        # Changing field 'Carosel.authors'
        db.alter_column('carosel_carosel', 'authors_id', self.gf('django.db.models.fields.related.ForeignKey')(default='default', to=orm['author.Author']))

    def backwards(self, orm):
        # Adding field 'CaroselImage.carosel'
        db.add_column('carosel_caroselimage', 'carosel',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carosel.Carosel'], null=True),
                      keep_default=False)

        # Adding field 'CaroselImage.description'
        db.add_column('carosel_caroselimage', 'description',
                      self.gf('django.db.models.fields.TextField')(default='default'),
                      keep_default=False)

        # Adding field 'CaroselImage.title'
        db.add_column('carosel_caroselimage', 'title',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=50),
                      keep_default=False)

        # Adding field 'CaroselImage.slug'
        db.add_column('carosel_caroselimage', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='default', max_length=50, unique=True),
                      keep_default=False)

        # Deleting field 'Carosel.caroselimages'
        db.delete_column('carosel_carosel', 'caroselimages_id')


        # Changing field 'Carosel.authors'
        db.alter_column('carosel_carosel', 'authors_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['author.Author'], null=True))

    models = {
        'author.author': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Author', '_ormbases': ['pages.Page']},
            'dob': ('django.db.models.fields.DateField', [], {}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        'carosel.carosel': {
            'Meta': {'object_name': 'Carosel'},
            'authors': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['author.Author']"}),
            'caroselimages': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['carosel.CaroselImage']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'carosel.caroselimage': {
            'Meta': {'object_name': 'CaroselImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['author.Author']", 'null': 'True', 'through': "orm['carosel.Carosel']", 'symmetrical': 'False'})
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