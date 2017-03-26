# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='money_tracker',
    version=version,
    description='Money Track',
    author='August Infotech',
    author_email='info@augustinfotech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
