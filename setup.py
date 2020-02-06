# -{pip install -e .}
# -{twine upload dist/*}
# -{del dist\* | python %f sdist bdist_wheel}
"""
:copyright: (c) 2019 by K1DV5
:license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages

VERSION = '0.2.4'

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='tkinter-math',
    author="Kidus Adugna",
    author_email='kidusadugna@gmail.com',
    classifiers=[
    #     'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="render math on tkinter canvas",
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='docal, tkinter, math',
    packages=['tkinter_math'],
    url='https://github.com/K1DV5/tkinter-math',
    version=VERSION,
    # zip_safe=False,
)

