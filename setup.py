
import os
import setuptools

_here = os.path.abspath(os.path.dirname(__file__))


def _get_version():

    import re

    version_file = os.path.join(_here, "src", "lss", "__version__.py")

    main_ns = {}

    with open(version_file) as vf:
        exec(vf.read(), main_ns)
        version = main_ns['__version__']

    if not version:
        raise RuntimeError("Unable to find version string in %s." % (version_file,))

    return version


_version = _get_version()


# Get the long description from the README file
with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

descript = ('A personal project for implementing behaviour akin to`ls` in '
            'addition to condensing sets of image sequences into a format '
            'that is easier to visualise to the user from the command line')

setuptools.setup(
    name="lsseq-jc",
    version=_version,

    author="Johnny Cochrane",
    author_email="johnny.p.cochrane@gmail.com",

    description=descript,
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/uncojohnco/eg--lsseq/",

    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],

    python_requires='>=3.8',

    scripts=['bin/lss']

)
