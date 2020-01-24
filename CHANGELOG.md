# CHANGELOG for django-popup-view-field

## 0.6.0 (2020-01-23)

* Added support for Django 2.2

* Drop support for Django 1.8

* Added support for bootstrap4 (testing only with Django >= 2.1)

* Added setting DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK

* Templates for widgets was splitted to blocks
  (for easy customization). Now `PopupViewWidget` can use
  template for bootstrap3 or template for bootstrap4

## 0.5.0 (2019-04-17)

* Support for Django 2.0 and 2.1

* Added PopupViewModelField that returns a model instance instead of text

## 0.4.1 (2019-02-23)

* Added `attrs` attribute to PopupViewField which is passed to the Widget

## 0.4.0 (2018-10-04)

* Added `callback_data` attribute to PopupViewField (read more in README)

## 0.3.0 (2017-03-07)

* Support for Django 1.11

## 0.2.0 (2017-02-20)

* Remove PopupViewField from django_popup_view_field.__init__,
  now you must import PopupViewField from django_popup_view_field.fields

* Sorting imports using isort

* Checking the order of imports in the tox

* Checking support for django-bootstrap3 v8.1.0

* Added django-bootstrap3 v8.1.0 to tox

* Adding version in django_popup_view_field.__init__

## 0.1 (2016-12-27)

* Initial version + tests + Travis CI
