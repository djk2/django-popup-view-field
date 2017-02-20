from django.template import Context, Library, loader
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def django_popup_view_field_javascript():
    """
    Return HTML for django_popup_view_field JavaScript.
    Adjust url in settings.

    **Tag name**::
        django_popup_view_field_javascript

    **Usage**::
        {% django_popup_view_field_javascript %}
    """
    temp = loader.get_template('django_popup_view_field/scripts_include.html')
    return temp.render({})
