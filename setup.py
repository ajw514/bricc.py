from setuptools import setup

setup(
    name = 'bricc',
    version = '0.1',
    description = 'Python wrapper around the Bricc conversion coefficent calculator',
    author = 'Andrew Ward',
    author_email = 'aw@ns.ph.liv.ac.uk',
    license = 'MIT',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Scientific/Engineering :: Physics'],
    keywords = ['internal conversion'],
    install_requires=['uncertainties'],
    py_modules = ['bricc'],
    )
