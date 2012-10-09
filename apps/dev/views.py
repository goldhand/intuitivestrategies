from django.shortcuts import render_to_response, render
from mezzanine.utils.views import render, paginate
from django.template import RequestContext
from .models import *
from mezzanine.twitter.models import *
import re
from settings import PROJECT_ROOT
from .forms import *
from django.http import HttpResponseRedirect


def re_term(results):
	re_item = re.findall('(Tweet: \w*): (.*?)\<a href', str(results))
	return str(re_item)

def TwitterTool(request, r_title=None):
	query = Query.objects.create(type="search", value="#"+r_title)
	query.run()
	unedited = query.tweets.get_query_set()[:100]
	unedited = str(unedited)
	results = re_term(unedited)
	return render_to_response('twitterapp.html', {'results':results, 'unedited':unedited}, context_instance = RequestContext(request))
	
def DadsAgain(request):
	return render_to_response('dadsagain.html', context_instance = RequestContext(request))


def Dev(request, ffamily=None, fcolor=None, fsize=None):
	if request.method == "POST":
		styleForm = EditStyle(request.POST)
		if styleForm.is_valid():
			ffamily = styleForm.cleaned_data['font_family']
			fsize = styleForm.cleaned_data['font_size']
			fcolor = styleForm.cleaned_data['font_color']
			if ffamily:
				ffamily_url = (ffamily.split(', '))[0].replace(' ', '+').strip("'")
				return HttpResponseRedirect('/dev/'+ffamily_url+'_'+str(fcolor)+'_'+str(fsize))
	else:
		styleForm = EditStyle()
	ffamily = ffamily
	fcolor = fcolor
	fsize = fsize
	if ffamily:
		ffamily_url = ffamily.replace('+', ' ')
	else:
		ffamily_url = ''
	return render(request, 'dev.html', {
		'ffamily':ffamily,
		'fcolor':fcolor,
		'fsize':fsize,
		'styleForm':styleForm,
		'ffamily_url':ffamily_url,

})
	
#def contact(request):
#	if request.method == 'POST':
