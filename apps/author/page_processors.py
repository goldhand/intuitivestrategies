
from djnago import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import *
#from myproject.apps.carosel.models import *

class AuthorForm(forms.Form):
	name		= forms.CharField()
	email		= forms.EmailField()


@processor_for(author)
def author_form(request, page):
	form = AuthorForm()
	if request.method == "POST"
		form = AuthorForm(request.POST)
		if form.is_valid():
			redirect = request.path + "?submitted=true"
			return HttpResponseRedirect(redirect)
		return {"form": form}

'''
@processor_for(Author)
def carosel_item(request, page):
	carosel_list = Carosel.objects.get(slug='author-carosel').caroselimage_set.all()
	return {'carosel_list': carosel_list}

'''

