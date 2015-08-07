from setuptools import setup, find_packages

setup(name='Mifkit',
      version='1.0.0',
      description='Tools for working with the Materials Information File (MIF).',
      author='Kyle Michel',
      author_email='kyle@citrine.io',
      packages=find_packages(),
      install_requires=[
          'requests'
      ])