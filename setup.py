from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'Python_BMP',
	  version 			= '1.0.0',
	  author			= 'Coding World',
	  author_email		= 'samuel@codingworld.eu',
	  description		= 'Library zum Auslesen des BMP mit Python3',
	  license			= 'MIT',
	  url				= 'https://github.com/coding-world/Python_BMP',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
	  install_requires	= ['Adafruit-GPIO>=0.6.5'],
	  packages 			= find_packages())
