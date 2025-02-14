from setuptools import setup, find_packages
import re
import os

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, 'README.md'), 'r') as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ''

try:
    with open(os.path.join(here, 'panoptes_aggregation/version/__init__.py'), 'r') as fp:
        version_file = fp.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M
    )
    if version_match:
        VERSION = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")
except FileNotFoundError:
    VERSION = '0.0.0'


setup(
    name='panoptes_aggregation',
    python_requires='>=3',
    version=VERSION,
    description='Aggregation code for Zooniverse panoptes projects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License'
    ],
    url='https://github.com/zooniverse/aggregation-for-caesar',
    author='Coleman Krawczyk',
    author_email='coleman@zooniverse.org',
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'panoptes_aggregation = panoptes_aggregation.scripts.aggregation_parser:main'
        ],
        'gui_scripts': [
            'panoptes_aggregation_gui = panoptes_aggregation.scripts.gui:gui'
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        'online': [
            'flask>=1.0,<2.1',
            'flask-cors>=3.0,<3.1',
            'panoptes-client>=1.1,<1.5',
            'requests>=2.4.2,<2.26',
            'gunicorn>=20.0,<20.2',
            'sentry-sdk[flask]>=0.13.5,<1.2',
            'newrelic>=5.4.0,<6.4.1',
            'gitpython>=3.0.0,<3.2'
        ],
        'doc': [
            'recommonmark>=0.5.0,<0.8',
            'sphinx>=2.2.2,<4.1',
            'sphinxcontrib-httpdomain>=1.7.0,<1.8',
            'sphinx_rtd_theme>=0.4.3,<0.6'
        ],
        'test': [
            'nose>=1.3.7,<1.4',
            'coverage>=4.5.3,<5.6',
            'coveralls>=3.0.0,<3.1.1',
            'flake8>=3.7,<3.10',
            'flake8-black>=0.1.1,<0.3',
            'flake8-bugbear>=20.1.2,<21.5'
        ],
        'gui': [
            'Gooey>=1.0.3,<1.1'
        ]
    },
    install_requires=[
        'beautifulsoup4>=4.8.1,<4.10',
        'collatex>=2.2,<2.3',
        'hdbscan>=0.8.20,<0.8.28',
        'lxml>=4.4,<4.7',
        'numpy>=1.20.0,<1.20.4',
        'packaging>=20.1,<20.10',
        'pandas>=1.0.0,<1.2.5',
        'progressbar2>=3.39,<3.54',
        'python-levenshtein>=0.12.0,<0.13',
        'python-slugify>=3.0.0,<5.1',
        'pyyaml>=5.1,<5.5',
        'scikit-learn>=0.21.1,<0.24.3',
        'scipy>=1.2,<1.6.4',
        'werkzeug>=0.14,<2.0.2'
    ]
)
