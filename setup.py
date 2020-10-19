import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wiki-parser",
    version="0.0.1",
    author="Maxim Razhev",
    author_email="cvlt.mao@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        'wikitextparser',

    ]
)