
from setuptools import setup

setup(name='sabnzbd_copy',
      version='0.1',
      description='sabnzbd copy script',
      url='http://github.com/xabgesagtx/sabnzbd_copy',
      author='xabgesagtx',
      author_email='xabgesagtx@riseup.net',
      license='MIT',
      packages=['sabnzbd_copy'],
      scripts= [
         'bin/sabnzbd-copy'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
