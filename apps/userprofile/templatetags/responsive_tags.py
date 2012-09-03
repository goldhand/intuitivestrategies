from django import template
from apps.userprofile.models import UserProfile
from mezzanine.blog.models import BlogPost
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


register = template.Library()


@register.filter(needs_autoescape=True)
def responsive(value, arg, autoescape=None):
	if autoescape:
		esc = conditional_escape
	else:
		esc = lambda x: x

	l = value.userprofile.limage.url
	d = value.userprofile.dimage.url
	t = value.userprofile.timage.url
	p = value.userprofile.thumbnail.url

	result = '<img class="visible-largedesktop %s" src="%s"/><img class="visible-desktop %s" src="%s" /><img class="visible-tablet %s" src="%s" /><img class="visible-phone %s" src="%s" />' % (esc(arg), esc(l), esc(arg), esc(d), esc(arg), esc(t), esc(arg), esc(p))
	
	return mark_safe(result)


