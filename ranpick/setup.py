import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ranpick", 
    version="0.1.0", 
    author="raimy5810", 
    author_email="yhg4908@kakao.com", 
    description="Generates a random numbe", 
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown",
    url="https://github.com/yhg4908/ranpick.py/",
    include_package_data=True,
    packages = setuptools.find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12", 
    install_requires=[], 
)
