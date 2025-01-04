"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import setuptools

about = {}
with open("svg_turtle/about.py") as f:
    exec(f.read(), about)

# noinspection PyUnresolvedReferences
setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    url=about['__url__'])
