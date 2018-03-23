from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'authentication-code-generator',
    version = '1.0.0',
    keywords = ('flexible', 'userful',"authentication code generator for python application"),
    description = "a simple library  to help you to generate authentication code. It's useful and flexible and convenient.",
    license = 'MIT License',
    author = 'andrewpqc',
    author_email = 'andrewpqc@mails.ccnu.edu.cn',
    packages = find_packages(),
    platforms = 'any',
)