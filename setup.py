"""Setup"""

from setuptools import setup

def readme():
    """Readme"""
    with open("README.rst") as rhand:
        return rhand.read()

setup(name='Line of Balance',
      version='1.0',
      description='Plot Line of Balance curve',
      long_description=readme(),
      classifiers=[
          'Developement Status :: 3 - Alpha',
          'Programming Language :: Python :: 3.6.1',
          'Topic :: Construction :: Project management',
      ],
      keywords='plot line of balance curve, diagram',
      url='',
      author='Chidi Orji',
      author_email='orjichidi95@gmail.com',
      license='MIT',
      packages=['pygit'],
      install_requires=[
          'matplotlib', 'numpy', 'openpyxl'
      ],
      zip_safe=False,
      test_suite='nose2.collector.collector',
      test_requires=["nose2"])
