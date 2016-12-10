# django-popup-view-field
Field and widget can render bootstrap dialog window with content from django view.


- Support for :

    * Python: 2.7, 3.4
    * Django: 1.8, 1.9, 1.10
    * django-crispy-forms
    * django-bootstrap3

- Require:

    * Django
    * django-bootstrap3 or django-crispy-forms
    * bootstrap3
    * JQuery

- Supported locale:

    * EN - (english)
    * PL - (polish)


The first version will be available in next week, after 20 December 2016
-------------------------------------------------------------------------


DO OPISANIA:
------------

* Mimifikacja JS

* Zainstalować aplikację
* Dodać do INSTALLED_APPS
* Dodać do głównych urls.py :
    url(r'^django_popup_view_field/', include( 'django_popup_view_field.urls', namespace="django_popup_view_field")),

* Zaimportować w głównym szablonie {% load django_popup_view_field_tags %}
* Dodać tag do głównego szablonu po skryptach dla bootstrap i jquery
* Utworzyć popup view
* Zarejestrować widok : registry_popup_view.register(AgePopupView)
* Utworzyć formularz i dodać do niego pole typu PopupViewField
    * view_class
    * popup_dialog_title


* Dla crispy pamiętać o wpisie w settings :
    CRISPY_TEMPLATE_PACK = "bootstrap3"

* Dla obsługi lokali dodać w settings middleware:
    'django.contrib.sessions.middleware.SessionMiddleware',
    ---> 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',

* Wymagane 'bootstrap3' lub 'crispy_forms' w INSTALLED_APPS

* Opisać sposób obsługi linków i form w popup view i restrykcje
  zwrócić uwagę na konieczność by linki i formy odwoływały się
  do lokalnej domeny, jak budować url dla linków i action w form
