from django.conf.urls import patterns

from .forms import ContactForm1, ContactForm2
from .views import ContactWizard

urlpatterns = patterns('',
    (r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2])),
)
