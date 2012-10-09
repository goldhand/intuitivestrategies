from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("apps.dadsagin.views",
        url("^dadsagain$", "Home"),
)

