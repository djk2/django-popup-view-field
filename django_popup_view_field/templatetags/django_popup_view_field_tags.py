from django.template import Library, loader
from django.conf import settings


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


@register.simple_tag
def django_popup_view_field_bootstrap_version():
    """
    Return value of DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK setting
    By default return `bootstrap3`
    Is used in `templates/scripts_include.html` to decide which js or html
    should be load

     **Tag name**::
        django_popup_view_field_bootstrap_version

    **Usage**::
        {% django_popup_view_field_bootstrap_version as bv %}
        {% if bv == 'bootstrap4' %}
            ...
        {% endif %}
    """
    return getattr(
        settings,
        'DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK',
        'bootstrap3'
    )
