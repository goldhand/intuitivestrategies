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

	l = value.limage.url
	d = value.dimage.url
	t = value.timage.url

	result = '<img class="visible-largedesktop %s" src="%s" alt="%s"/><img class="visible-desktop %s" src="%s" alt="%s"/><img class="visible-tablet %s" src="%s" alt="%s"/>' % (esc(arg), esc(l), esc(value), esc(arg), esc(d), esc(value), esc(arg), esc(t), esc(value))
	
	return mark_safe(result)


