# -{twine upload dist/*}
# -{del dist\* | python %f sdist bdist_wheel}
# -{pip install -e .}
"""
:copyright: (c) 2019 by K1DV5
:license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages

VERSION = '0.2.2'

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Kidus Adugna",
    author_email='kidusadugna@gmail.com',
    # classifiers=[
    #     'Development Status :: 5 - Production/Stable',
    #     'Intended Audience :: Developers',
    #     'Intended Audience :: End Users/Desktop',
    #     'License :: OSI Approved :: MIT License',
    #     'Natural Language :: English',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.6',
    #     'Programming Language :: Python :: 3.7',
    # ],
    description="render math on tkinter canvas",
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='docal',
    name='tkinter-math',
    packages=['tkinter_math'],
    # url='https://github.com/K1DV5/docal',
    version=VERSION,
    # zip_safe=False,
)

