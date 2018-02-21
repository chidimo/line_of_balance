"""Setup"""

from setuptools import setup

# pip install https://github.com/Parousiaic/line_of_balance/archive/master.zip

def readme():
    """Readme"""
    with open("README.md") as rhand:
        return rhand.read()

setup(name='lineofbalance',
      version='2.0',
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
      packages=['line_of_balance'],
      install_requires=[
          'matplotlib', 'numpy', 'openpyxl'
      ],
      zip_safe=False,
      test_suite='nose2.collector.collector',
      test_requires=["nose2"])
