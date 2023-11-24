from setuptools import setup, find_packages

setup(
    name='your-package-name',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
)
