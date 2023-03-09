from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'EDSA practice example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/<raveex12>/<explorepracticeexample>',
    author = '<Festus Godwin>',
    author_email = '<godwinfestus8@gmail.com>'
    
)