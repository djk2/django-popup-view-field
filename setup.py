# encoding:utf-8
from setuptools import setup, find_packages
from django_popup_view_field import __version__ as version


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-popup-view-field',
    version=version,
    description='Field and widget can render bootstrap dialog window with content from django view',
    url='https://github.com/djk2/django-popup-view-field',
    author='Grzegorz Tężycki',
    author_email='grzegorz.tezycki@gmail.com',
    long_description=readme(),
    license='MIT',
    packages=find_packages(exclude=['docs']),
    package_data={'django_popup_view_field': [
        'templates/django_popup_view_field/*',
        'static/django_popup_view_field/js/*',
        'locale/pl/LC_MESSAGES/*'
    ]},
    tests_require=['Django', 'django-bootstrap3', 'django-crispy-forms'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django>=1.8'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    keywords='popup crispy bootstrap views',
)
