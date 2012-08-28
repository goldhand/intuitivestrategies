# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field images on 'Carosel'
        db.delete_table('carosel_carosel_images')

        # Adding field 'CaroselImage.carosels'
        db.add_column('carosel_caroselimage', 'carosels',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carosel.Carosel'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding M2M table for field images on 'Carosel'
        db.create_table('carosel_carosel_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('carosel', models.ForeignKey(orm['carosel.carosel'], null=False)),
            ('caroselimage', models.ForeignKey(orm['carosel.caroselimage'], null=False))
        ))
        db.create_unique('carosel_carosel_images', ['carosel_id', 'caroselimage_id'])

        # Deleting field 'CaroselImage.carosels'
        db.delete_column('carosel_caroselimage', 'carosels_id')


    models = {
        'carosel.carosel': {
            'Meta': {'object_name': 'Carosel'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'carosel.caroselimage': {
            'Meta': {'object_name': 'CaroselImage'},
            'carosels': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['carosel.Carosel']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carosel']