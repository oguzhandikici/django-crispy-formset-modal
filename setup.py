#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-crispy-formset-modal",
    packages=["crispy_formset_modal"],
    include_package_data=True,
    version="0.6",
    description="Django app that provides an easy way to manage and manipulate formsets using modals with Django Crispy Forms.",
    long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
    author="Blas Fernandez",
    author_email="blasferna@gmail.com",
    url="https://github.com/blasferna/django-crispy-formset-modal",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=["Django>=3.2"],
    python_requires=">=3.7",
)
