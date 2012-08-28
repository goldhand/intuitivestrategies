# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CaroselImage'
        db.create_table('carosel_caroselimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('carosel', ['CaroselImage'])

        # Adding model 'Carosel'
        db.create_table('carosel_carosel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('carosel', ['Carosel'])

        # Adding M2M table for field images on 'Carosel'
        db.create_table('carosel_carosel_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('carosel', models.ForeignKey(orm['carosel.carosel'], null=False)),
            ('caroselimage', models.ForeignKey(orm['carosel.caroselimage'], null=False))
        ))
        db.create_unique('carosel_carosel_images', ['carosel_id', 'caroselimage_id'])


    def backwards(self, orm):
        # Deleting model 'CaroselImage'
        db.delete_table('carosel_caroselimage')

        # Deleting model 'Carosel'
        db.delete_table('carosel_carosel')

        # Removing M2M table for field images on 'Carosel'
        db.delete_table('carosel_carosel_images')


    models = {
        'carosel.carosel': {
            'Meta': {'object_name': 'Carosel'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['carosel.CaroselImage']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'carosel.caroselimage': {
            'Meta': {'object_name': 'CaroselImage'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carosel']