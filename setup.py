from setuptools import setup, find_packages

setup(
    name='ranpick',
    version='3.1.0',
    author='rainy58',
    author_email='yhg4908@naver.com',
    description='A high-entropy random number generation library',
    long_description=open('README.md').read() if open('README.md', 'r').read() else '',
    long_description_content_type='text/markdown',
    project_urls={
        "Issues": "https://github.com/yhg4908/ranpick.py/issues",
        "Repository": "https://github.com/yhg4908/ranpick.py",
    },
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    license = "MIT",
    python_requires='>=3.7',
    package_data={'': ['LICENSE', 'README.md', 'README_KR.md']},
    keywords='random number generation entropy ranpick list Probability',
)
