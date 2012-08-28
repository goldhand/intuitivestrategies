from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Post
from django.contrib.syndication.views import Feed

urlpatterns = patterns('irawcc.views',


	url(r'^$', 'Home'), 
	url(r'^blog/', include("blog.urls")),
	url(r'^about/', 'About'),
	url(r'^work/', 'Work'),
	url(r'^media/', 'Media'),
	url(r'^archives/', 'Archives'),
	url(r'^contact/', 'Contact'),
	url(r'^get-involved/', 'GetInvolved'),
#	url(r'^(?P<pk>\d+)$', DetailView.as_view(
#			model=Post,
#			template_name="post.html")),
#	url(r'^archives/$', ListView.as_view(
#			queryset=Post.objects.all().order_by("-created"),
#			template_name="archives.html")),	
#	url(r'^about/$', 'aboutpage'),
#	url(r'^about/$', TemplateView.as_view(
#			template_name="about.html")),

#	url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
#	url(r'^feed/$', BlogFeed()),
	

)
