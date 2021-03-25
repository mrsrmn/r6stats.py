import setuptools

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name="r6stats.py",
    version="1.0.1",
    author="MakufonSkifto",
    description="A Python wrapper for the R6Stats.com API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/MakufonSkifto/r6stats.py",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="r6stats api siege r6siege",
    python_requires='>=3.0',
)
