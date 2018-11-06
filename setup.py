# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon web service application programming interface (API).   # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "tkbeacon"
VERSION = "1.3.0.post1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Translator Knowledge Beacon API",
    author_email="richard@starinformatics.com",
    url="https://github.com/NCATS-Tangerine/tkbeacon-python-client",
    keywords=["Swagger", "Translator Knowledge Beacon API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Translator Knowledge Beacon web service application programming interface (API).
    """
)
