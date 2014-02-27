from distutils.core import setup
import os


setup(name='django-contact-us',
      version='1.0',
      description='Generic contact-us application for Django',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read(),
      author='Maximiliano Cecilia',
      author_email='maxicecilia@gmail.com',
      url='https://bitbucket.org/ubernostrum/django-contact-form/',
      packages=['contact_us'],
      download_url='http://bitbucket.org/ubernostrum/django-contact-form/downloads/django-contact-form-1.0.tar.gz', 
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      )
