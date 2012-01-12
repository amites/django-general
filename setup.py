from setuptools import setup, find_packages

version = '1.0'

LONG_DESCRIPTION = """
Various snippets compiled for re-use.
"""

setup(
    name='django-general',
    version=version,
    description="django-general",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='general,django',
    author='Alvin Mites',
    author_email='alvin@mitesdesign.com',
#    url='http://github.com/ericflo/django-avatar/',
#    license='BSD',
    packages=find_packages(),
    package_data = {
        'general': [
            'fixtures/*'
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
