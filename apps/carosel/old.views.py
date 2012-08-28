from pages.models import Page
from carosel.models import Carosel
from django.shortcuts import render_to_response


def Home(request):
	page_items = Page.objects.get(slug='home')
        page_contents = page_items.pagecontent_set.all().order_by('position')
       	carosel_list	= Carosel.objects.filter(destination='http://webpowerlabs.com/irawcc')[:3]

	farticle_list           = Article.objects.filter(featured=True).order_by('-created')
        farticle                = farticle_list[0]
	
	fimage_list		= Image.objects.filter(featured=True).order_by('-created')
        fimage			= fimage_list[0]

	posts = Post.objects.all().order_by('-created')[:8]

	return render_to_response('layouts/home.html', {'page':page_items, 'page_contents':page_contents, 'carosel_list': carosel_list, 'farticle':farticle, 'posts':posts, 'fimage':fimage})


