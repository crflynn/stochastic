"""Setup."""
import io
from os import path
from setuptools import find_packages
from setuptools import setup


here = path.abspath(path.dirname(__file__))

# io.open for py27
with io.open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

# import __version__ attributes
about = {}
with open(path.join(here, "stochastic", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    license=about["__license__"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords="stochastic processes",
    packages=["stochastic"],
    package_dir={"stochastic": "stochastic"},
    install_requires=[
        "numpy",
        "scipy",
    ],
    include_package_data=True,
    zip_safe=False
)
