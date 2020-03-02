#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'sentry==9.1.2',
]

setup(
    name='sentry-feishu',
    version='0.0.1',
    keywords='sentry feishu',
    author='AdamWang',
    author_email='wangbinhan@xiaoduotech.com',
    url='https://github.com/AdamWangDoggie/sentry-feishu',
    description='A Sentry extension which integrates with feishu robot.',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'feishu = sentry_feishu.plugin:FeishuPlugin'
        ],
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
