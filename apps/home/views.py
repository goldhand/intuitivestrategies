#from pages.models import Page
from apps.carosel.models import Carosel
from django.shortcuts import render_to_response
from django.template import RequestContext
#from news.models import Article
#from blog.models import Post
#from mediaviewer.models import *


def Home(request, slug):
#	page_items 		= Page.objects.get(slug='home')
#        page_contents 		= page_items.pagecontent_set.all().order_by('position')
       	carosel_list		= Carosel.objects.all()[:3]
	
#	farticle_list           = Article.objects.filter(featured=True).order_by('-created')
#        farticle                = farticle_list[0]
	
#	fimage_list		= Image.objects.filter(featured=True).order_by('-created')
 #       fimage			= fimage_list[0]

#	posts = Post.objects.all().order_by('-created')[:8]

#	return render_to_response('layouts/home.html', {'page':page_items, 'page_contents':page_contents, 'carosel_list': carosel_list, 'farticle':farticle, 'posts':posts, 'fimage':fimage},context_instance = RequestContext(request))
	return render_to_response('index.html', {'carosel_list': carosel_list})


'''
def About(request):
	page_items = Page.objects.get(slug='about')
        page_contents = page_items.pagecontent_set.all().order_by('position')
	return render_to_response('about.html', {'page':page_items, 'page_contents':page_contents})


def Work(request):
	page_items = Page.objects.get(slug='work')
        page_contents = page_items.pagecontent_set.all().order_by('position')

	return render_to_response('about.html', {'page':page_items, 'page_contents':page_contents})



def Media(request):
	page_items = Page.objects.get(slug='media')
        page_contents = page_items.pagecontent_set.all().order_by('position')

	return render_to_response('about.html',{'page':page_items, 'page_contents':page_contents})


def Archives(request):
	page_items = Page.objects.get(slug='archives')
        page_contents = page_items.pagecontent_set.all().order_by('position')

	return render_to_response('about.html', {'page':page_items, 'page_contents':page_contents})


def Contact(request):
	page_items = Page.objects.get(slug='contact')
        page_contents = page_items.pagecontent_set.all().order_by('position')


	return render_to_response('about.html', {'page':page_items, 'page_contents':page_contents})


def GetInvolved(request):
	page_items = Page.objects.get(slug='get-involved')
        page_contents = page_items.pagecontent_set.all().order_by('position')

	return render_to_response('about.html', {'page':page_items, 'page_contents':page_contents})


'''

