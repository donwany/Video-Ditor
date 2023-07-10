from setuptools import find_packages, setup

with open("README.md") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(
    name="video-ditor",
    py_modules=["cut", "background", "concat", "watermark", "download", "add_text"],
    version="0.0.3",
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/donwany/video-ditor.git",
    license="MIT License",
    author="Theophilus Siameh",
    author_email="theodondre@gmail.com",
    install_requires=install_requires,
    description="A python package to manipulate videos",
    entry_points={
        "console_scripts": [
            "slice = cut.main:cli",
            "concat = concat.main:cli",
            "background = background.main:cli",
            "watermark = watermark.main:cli",
            "ytube = download.main:cli",
            "add_text = add_text.main:cli",
        ]
    },
    classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    keywords="video editor, editor, video manipulator, cut videos, join videos, add watermark to videos",
    platforms=["any"],
    python_requires=">=3.7",
)
