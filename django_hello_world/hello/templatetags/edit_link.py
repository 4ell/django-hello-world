from django import template
from django.core import urlresolvers


register = template.Library()

@register.simple_tag
def edit_link(enity):
	try:
		path = "admin:{app}_{model}_change"
		return urlresolvers.reverse(
			path.format(
				app=enity._meta.app_label,
				model=enity._meta.object_name
			).lower(),
			args=(enity.id,)
		)
	except:
		return None