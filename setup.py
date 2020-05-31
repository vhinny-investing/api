import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vhinny", # Replace with your own username
    version="0.0.7",
    author="Vitalii Dodonov",
    author_email="admin@vhinny.com",
    description="Vhinny Financial Data API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vhinny-investing/api",
    packages=['vhinny'],
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)