#!/usr/bin/env python

from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup, find_packages

install_requirements = parse_requirements('requirements.txt', session=PipSession())
requirements = [str(ir.req) for ir in install_requirements]

config = {
    'name': 'project',
    'description': 'Project example',
    'download_url': '',
    'version': '1.0.0',
    'install_requires': requirements,
    'test_require': [
        'nose==1.3.7',
        'mock==1.3.0',
        'requests-mock==1.3.0'
    ],
    'packages': find_packages(exclude=['tests*'])
}

setup(**config)