import sys

from setuptools import setup, find_packages

try:
    import multiprocessing
    import logging
except:
    pass

requires = [
    "tw2.core>=2.0b2",
    "tw2.forms",
]
tests_require = [
    'nose',
    'mako',
]


if sys.version_info[0] < 3:
    tests_require.append('FormEncode')


f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

# Requirements to install buffet plugins and engines
_extra_genshi = ["Genshi >= 0.3.5"]
_extra_mako = ["Mako >= 0.1.1"]

setup(
    name='tw2.jquery',
    version='2.2.0.2',
    description="toscawidgets2 wrapper for jQuery",
    long_description=long_description,
    author='Joseph Tate',
    author_email='jtate@dragonstrider.com',
    license='MIT',
    url='http://github.com/toscawidgets/tw2.jquery',
    install_requires=requires,
    extras_require = {
        'genshi': _extra_genshi,
        'mako': _extra_mako,
    },
    tests_require=tests_require,
    packages=['tw2', 'tw2.jquery'],
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jquery
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'License :: OSI Approved :: MIT License',
    ],
)
