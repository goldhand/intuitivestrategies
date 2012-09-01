from django.db import models
from mezzanine.pages.models import Page
from django.utils.translation import ugettext_lazy as _


def uploadconverter(

class UploadFile(Page):
	
	content		= models.FileField(upload_to="files", null=True)

f = open(UploadFile.content, "r")
content_text = f.read();


