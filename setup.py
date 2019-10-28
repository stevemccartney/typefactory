from setuptools import setup


setup(
    name="TypeFactory",
    version="0.1.0dev",
    author="Steve McCartney",
    author_email="python+typefactory@reconvergent.com",
    url="https://github.com/stevemccartney/typefactory",
    packages=["typefactory"],
    license="Apache-2.0",
    description="Simplify the creation and utilisation of typed and constrained value objects in Python 3",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Typing :: Typed",
    ],
)
