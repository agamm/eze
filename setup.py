from setuptools import setup, find_packages

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='flick',
    version='0.0.1',
    url='https://github.com/agamm/flick',
    long_description=readme,
    long_description_content_type='text/markdown',

    description='Modern minimalist python 3+ pocket knife.',
    author='agamm',
    maintainer='Agam More',
    license='MIT',
    packages=find_packages(exclude=('*_test.py')),
    classifiers=[
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[],
    zip_safe=False,
)