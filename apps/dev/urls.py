
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("apps.dev.views",
	url("^dadsagain$", "DadsAgain"),
#	url("^(?P<ffamily>.*?)_(?P<fcolor>.*?)_(?P<fsize>.*?)/$", "Dev"),
	url("^(?P<r_title>.*)/$", "TwitterTool"),
	url("^$", "Dev")
)
