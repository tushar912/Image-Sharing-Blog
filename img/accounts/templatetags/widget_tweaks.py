from django import template

register = template.Library()


@register.filter
def add_class(form_widget, css_class):
	
	return form_widget.as_widget(attrs={'class': css_class})