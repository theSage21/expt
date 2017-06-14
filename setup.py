from setuptools import setup
from expt import __version__
__version__ = list(map(str, __version__))


setup(name='expt',
      version='.'.join(__version__),
      description='Experiment Manager',
      url='http://github.com/theSage21/expt',
      author='Arjoonn Sharma',
      author_email='arjoonn.94@gmail.com',
      license='MIT',
      packages=['expt'],
      install_requires=['ipython', 'jupyter'],
      entry_points={'console_scripts': ['expt=expt.cli:main']},
      keywords=['expt', 'manager', 'experiment', 'hypothesis', 'notebook'],
      zip_safe=False)
