# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

extras_require = {
    'test': [
        "pytest==6.2.5",
        "pytest-xdist==1.26.0",
    ],
    'lint': [
        "flake8==3.5.0",
        "mypy==0.641",
        "mypy-extensions>=0.4.1",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "twine",
    ],
}


extras_require['dev'] = (
    extras_require['dev'] +
    extras_require['test'] +
    extras_require['lint']
)

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py_ecc',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='6.0.0',
    description='Elliptic curve crypto in python including secp256k1 and alt_bn128',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Vitalik Buterin',
    author_email='',
    url='https://github.com/ethereum/py_ecc',
    license="MIT",
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'py_ecc': ['py.typed']},
    install_requires=[
        "eth-typing>=3.0.0,<4",
        "eth-utils>=2.0.0,<3",
        "mypy-extensions>=0.4.1",
        "cached-property>=1.5.1,<2",
    ],
    python_requires='>=3.6, <4',
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
