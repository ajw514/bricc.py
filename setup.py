from setuptools import setup

setup(
    name = 'bricc',
    version = '0.1.0',
    description = 'Python wrapper around the Bricc conversion coefficent calculator',
    author = 'Andrew Ward',
    author_email = 'aw@ns.ph.liv.ac.uk',
    url = 'https://github.com/ajw514/bricc',
    license = 'MIT',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3'],
    keywords = ['internal conversion'],
    install_requires=['uncertainties'],
    py_modules = ['bricc'],
    )
