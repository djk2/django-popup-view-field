django-popup-view-field
------------------------

.. image:: https://badge.fury.io/py/django-popup-view-field.svg
    :target: https://badge.fury.io/py/django-popup-view-field
    :alt: Latest PyPI version


.. image:: https://travis-ci.org/djk2/django-popup-view-field.svg?branch=master
    :target: https://travis-ci.org/djk2/django-popup-view-field
    :alt: Travis CI


.. image:: https://requires.io/github/djk2/django-popup-view-field/requirements.svg?branch=master
    :target: https://requires.io/github/djk2/django-popup-view-field/requirements/?branch=master
    :alt: Requirements Status


Field and widget can render bootstrap dialog with content from django view.
You can create normal django View and load this view in dialog for form field.

- Support:

    * Python: 2.7, 3.6
    * Django: 1.8, 1.9, 1.10, 1.11
    * django-crispy-forms
    * django-bootstrap3

- Require:

    * Django
    * bootstrap3
    * JQuery

- Recommended:

    * django-bootstrap3 or
    * django-crispy-forms

- Locale:

    * EN - (english)
    * PL - (polish)

- Tested on browsers:

    * OK - Google Chrome 70.0 - Fedora 28
    * OK - Firefox 62.0.3 - Fedora 28
    * OK - Firefox 50.1.0 - Ubuntu 14.04
    * OK - Firefox 31.1 - CentOS 6.4
    * OK - Chromium 53.0 - Ubuntu 14.04
    * OK - Microsoft Edge 38 - Windows 10
    * OK - Internet Explorer 11.0 - Windows 10
    * OK - Internet Explorer 10.0 - Windows 7
    * OK - Internet Explorer 9.0 - Windows 7
    * ER - Internet Explorer <= 8 (no support "html()" for data-popup-view-value)


Screenshots
------------

- Example: Form with several popup-view-fieds

.. image:: https://raw.githubusercontent.com/djk2/django-popup-view-field/master/doc/static/scr1.png
    :alt: Form with django-popup-view-fieds

- Example: Dialog for select sex

.. image:: https://raw.githubusercontent.com/djk2/django-popup-view-field/master/doc/static/scr2.png
    :alt: Dialog for select sex

- Example: Dialog for select color

.. image:: https://raw.githubusercontent.com/djk2/django-popup-view-field/master/doc/static/scr3.png
    :alt: Dialog for select color

- Example: Dialog with form

.. image:: https://raw.githubusercontent.com/djk2/django-popup-view-field/master/doc/static/scr4.png
    :alt: Dialog with form


Run demo
---------
1. Clone or download repository::

    git clone https://github.com/djk2/django-popup-view-field.git

2. Create virtualenv or not (red more: http://docs.python-guide.org/en/latest/dev/virtualenvs/)

3. Install requirements for demo::

    cd django-popup-view-field/demo

    pip install -r requirements.txt

4. Run developing web server::

    python manage.py runserver

5. Run your browser and call url: 127.0.0.1:8000 ::

    firefox 127.0.0.1:8000


Install
--------
Install package - There are several solutions, choose your own
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Install using pypi repository::

    pip install django-popup-view-field

2. Install using pip + github repository url::

        pip install git+https://github.com/djk2/django-popup-view-field.git

3. Install using pip + zip archive::

    wget https://github.com/djk2/django-popup-view-field/archive/master.zip
    pip install master.zip

4. Clone or download application to your django project directory::

    wget https://github.com/djk2/django-popup-view-field/archive/master.zip -O /tmp/master.zip
    unzip /tmp/master.zip -d /tmp/
    cd my_project_dir
    cp -r /tmp/django-popup-view-field-master/django_popup_view_field/ ./

Add ``django_popup_view_field`` to your INSTALLED_APPS setting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*settings.py* ::

    INSTALLED_APPS = [
        ...
        'bootstrap3',    # If you use django-bootstrap3
        'crispy_forms',  # If you user django-crispy-forms

        'django_popup_view_field',
        ...
    ]

**Warning**:
 Is recommended use django-bootstrap3 or django-crispy-forms
 to render forms and  fields, but this is not necessary.
 You can still write django templates using pure CSS from bootstrap3.
 More information about bootstrap forms in here: http://getbootstrap.com/css/#forms


Add the django_popup_view_field urls to your root url patterns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*urls.py* ::

    urlpatterns = [
        ...
        url(
            r'^django_popup_view_field/',
            include('django_popup_view_field.urls', namespace="django_popup_view_field")
        ),
    ]

**Note**:
 The URL path can be whatever you want,
 but you must include 'django_popup_view_field.urls' with the 'django_popup_view_field' namespace.
 You may leave out the namespace in Django >= 1.9


In your base template, add ``django_popup_view_field_javascript`` tag
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``django_popup_view_field_javascript`` template tag load all required javascripts and
template-scripst for application.
Tag should be append before body close </body> tag and after jQuery and Bootstrap scripts.

*base.html* ::

    <!DOCTYPE html>
    {% load django_popup_view_field_tags %}

    <html>
        <head>
            ...
            <!-- Bootstrap CSS should be here -->
            ...
        </head>

        <body>
            ...
            ...
            <!-- jQuery script should be here -->
            <!-- Bootstrap javascripts should be here -->
            ...
            ...
            {% django_popup_view_field_javascript %}
        </body>
    </html>


Simple Example
------------------------

.. image:: https://raw.githubusercontent.com/djk2/django-popup-view-field/master/doc/static/simple_example.png
    :alt: Simple Example - screenshot


Create PopupView
^^^^^^^^^^^^^^^^^

Html content rendered by this view will be loaded into bootstrap dialog.
Create your popup view same as normal django view.

| **Your popup view must be subclass of django.views.generic.View**

*templates/myapp/popups/colors.html* ::

    <ul>
        <li data-popup-view-value="red" style="background:red;"> red hat </li>
        <li data-popup-view-value="blue" style="background:blue;"> blue sky </li>
        <li data-popup-view-value="green" style="background:green;"> green planet </li>
        <li data-popup-view-value="pink" style="background:pink;"> pink car </li>
    </ul>

If user click on the element with the attribute ``data-popup-view-value``,
the value of this attribute will be set in form field and dialog will close.

|

If you want set content of element as value in form field, use ``html()`` for attribute::

    <li data-popup-view-value="html()"> This text will be use :) </li>

*popups.py* ::

    from django.views.generic import TemplateView
    from django_popup_view_field.registry import registry_popup_view

    class ColorsPopupView(TemplateView):
        template_name = 'myapp/popups/colors.html'

    # REGISTER IS IMPORTANT
    registry_popup_view.register(ColorsPopupView)

Remember that you must register your popup view.
After register you can run your popup view by call url::

    ..../django_popup_view_field/ColorsPopupView

In template you can get url to popup view using url tag::

    {% url "django_popup_view_field:get_popup_view" 'ColorsPopupView' %}

After register you can unregister your popup view::

    registry_popup_view.unregister(ColorsPopupView)

    # or unregister by view name

    registry_popup_view.unregister_by_name('ColorsPopupView')

You can also get popup view class by name::

    view_class = registry_popup_view.get('ColorsPopupView')
    view_class.as_view()


Create Form with PopupViewField
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*forms.py* ::

    from django import forms
    from django_popup_view_field.fields import PopupViewField
    from myapp.popups import ColorsPopupView

    class ColorForm(forms.Form):

        color = PopupViewField(
            view_class=ColorsPopupView,
            popup_dialog_title='What is your favorite color',
            attrs={'readonly': True},
            required=True,
            help_text='be honest'
        )

**class PopupViewField(view_class, popup_dialog_title, *args, **kwargs)**

* ``view_class`` - **required** - popup view class, view to render dialog content, must be subclass of django.views.generic.View
* ``popup_dialog_title`` - **not required** - Title for dialog, default ``Popup Dialog: Select value``
* ``attrs`` - **not required** - provides attributes for Widget
* ``args`` and ``kwargs`` are default for CharField


Create typical FormView
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*views.py* ::

    from django.views.generic import FormView
    from myapp.forms import ColorForm
    from django.http import HttpResponse

    class ColorFormView(FormView):
        template_name = "myapp/color_form.html"
        form_class = ColorForm

        def form_valid(self, form):
            color = form.cleaned_data.get("color")
            return HttpResponse("Your color: {0}".format(color))

**Template using django-crispy-forms**

*templates/myapp/color_form.html* ::

    {% extends "base.html" %}
    {% load crispy_forms_tags %}
    {% crispy form %}


**Template using django-bootstrap3**

*templates/myapp/color_form.html* ::

    {% extends "base.html" %}
    {% load bootstrap3 %}

    <form action="." method="post" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% buttons %}
            <button type="submit" class="btn btn-primary">Submit</button>
        {% endbuttons %}
    </form>

**Template with pure bootstrap3 css (without django-bootstrap3 and crispy)**

*templates/myapp/color_form.html* ::

    {% extends "base.html" %}
    <form action="." method="post" class="form">
        <div class="form-group">
            <label class="control-label"> {{ form.color.label }} </label>
            {{ form.color }}
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>


callback_data attribute
------------------------
If you want pass extra parameters to your popup view, you should use `callback_data`
attribute for PopupViewField. This argument should be dictionary or OrderedDict.
This dictionary containing yours parameters will be encoded to ASCII text string and
added to url address. In your popup view You can take this parameters from `request.GET`.

*popups.py* ::

    from django.views.generic import View
    from django_popup_view_field.registry import registry_popup_view

    class FooPopupView(View):
        def get(self, request):
            print(request.GET['extra_param'])  # --> will be "Foo Bar"
            print(request.GET['my_pk'])        # --> will be 666
            ....

    # REGISTER IS IMPORTANT
    registry_popup_view.register(FooPopupView)

*forms.py* ::

    from django import forms
    from django_popup_view_field.fields import PopupViewField

    class FooForm(forms.Form):

        some_field = PopupViewField(
            view_class=FooPopupView,
            callback_data={
                'extra_param': 'Foo Bar',
                'my_pk': 666
            }
        )



Advanced Example
------------------------

Advanced Example use django-bootstrap3.
Dialog is interactive, all links and forms will be send via Ajax and response will be loaded in dialog.

.. image:: https://raw.githubusercontent.com/djk2/django-popup-view-field/master/doc/static/advanced_example.png
    :alt: Advanced Example - screenshot


PopupView
^^^^^^^^^^

*templates/myapp/popups/alphabet.html* ::

    <h4> Select the first letter of your name </h4>

    {% for char in alphabet %}
        <div class="btn btn-xs btn-info" data-popup-view-value="html()">
            {{ char }}
        </div>
        {% if forloop.counter|divisibleby:"13" and forloop.counter > 0 %}
            <br/><br/>
        {% endif %}
    {% endfor %}

    {# Button to change order #}
    <a class="btn btn-xs btn-primary" style="margin-top:20px;"
              href="{% url "django_popup_view_field:get_popup_view" 'AlphabetPopupView' %}?direction={{direction}}">
        Reverse order
    </a>

**popups.py* ::

    from django.views.generic import TemplateView
    from django_popup_view_field.registry import registry_popup_view
    from string import ascii_uppercase

    class AlphabetPopupView(TemplateView):
        template_name = 'myapp/popups/alphabet.html'
        direction = 1

        def get_context_data(self, **kwargs):
            self.direction = int(self.request.GET.get("direction") or self.direction)
            alphabet = ascii_uppercase[::self.direction]
            ctx = super(AlphabetPopupView, self).get_context_data(**kwargs)
            ctx['alphabet'] = alphabet
            ctx['direction'] = self.direction * -1
            return ctx

    # REGISTER IS IMPORTANT
    registry_popup_view.register(AlphabetPopupView)


Form with PopupViewField
^^^^^^^^^^^^^^^^^^^^^^^^^^
*forms.py* ::

    from django import forms
    from django_popup_view_field.fields import PopupViewField
    from myapp.popups import AlphabetPopupView

    class AlphabetForm(forms.Form):

        char = PopupViewField(view_class=AlphabetPopupView, required=True)

View
^^^^^

*templates/myapp/alphabet.html* ::

    {% extends "base.html" %}
    {% load bootstrap3 %}

    <form action="." method="post" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% buttons %}
            <button type="submit" class="btn btn-primary">Submit</button>
        {% endbuttons %}
    </form>

*views.py* ::

    from django.views.generic import FormView
    from myapp.forms import AlphabetForm
    from django.http import HttpResponse

    class AlphabetFormView(FormView):
        template_name = "myapp/alphabet.html"
        form_class = AlphabetForm

        def form_valid(self, form):
            char = form.cleande_data.get("char")
            return HttpResponse("First letter of your name : {0}".format(char))


Others
---------
* Remember, if you use a django-crispy-forms then you should set CRISPY_TEMPLATE_PACK = "bootstrap3" in settings.py

* If you want change locale (Polish, English is supported) then you must add ``LocaleMiddleware`` to your settings.MIDDLEWARE::

    MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        ...
        'django.middleware.locale.LocaleMiddleware',
    ]

* More about bootstrap in here : http://getbootstrap.com/

* More about django-crispy-forms in here : http://django-crispy-forms.readthedocs.io/en/latest/

* More about django-bootstrap3 in here : http://django-bootstrap3.readthedocs.io/en/latest/

* Documentation prepared with the help of **Online reStructuredText editor** : http://rst.ninjs.org/
