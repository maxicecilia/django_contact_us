from distutils.core import setup
import os


setup(name='django-contact-us',
      version='1.0',
      description='Generic contact-us application for Django',
      long_description='Generic contact-us application for Django',
      author='Maximiliano Cecilia',
      author_email='maxicecilia@gmail.com',
      url='https://github.com/maxicecilia/django_contact_us/',
      packages=['contact_us'],
      download_url='http://github.com/maxicecilia/django_contact_us/downloads/django_contact_us-1.0.0.tar.gz',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      )
