
import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "__version__.py")) as version_file:
    exec(version_file.read())

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

descript = ('A personal project for implementing behaviour akin to`ls` in '
            'addition to condensing sets of image sequences into a format '
            'that is easier to visualise to the user from the command line')

setuptools.setup(
    name="lsseq-jc",
    version=__version__,  # noqa: F821

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

    test_suite="test.run",

)