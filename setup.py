from setuptools import setup

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="src",
    version="0.0.1",
    author="sam",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tammavarapu/dvc_test_pipeline",
    author_email="sambasiva.tammavarapu@gmail.com",
    packages=["src"],
    #license="GNU",
    python_requires=">=3.7",
    install_requires=[
        'dvc==2.7.3',
        'pandas',
        'scikit-learn'
    ]
)