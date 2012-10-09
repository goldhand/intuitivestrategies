from django import forms
from django.forms.extras import SelectDateWidget
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.forms import fields
from mezzanine.forms.models import FormEntry, FieldEntry



class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
