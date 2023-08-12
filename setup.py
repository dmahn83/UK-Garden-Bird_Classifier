import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='UK_Garden_Bird_Classifier',
    version='0.2.0',
    packages=setuptools.find_packages(where='src'),  # Point setuptools to the 'src' directory
    package_dir={'': 'src'},             # Specify that the root package is under 'src'
    description='A package for UK garden bird image classification.',
    author='David Mahony',
    author_email='dmahn83@gmail.com',
    url='',
    install_requires=[
        'tensorflow',
        'pillow',
        'matplotlib',
    ],
    classifiers=[  # Classifiers to categorize your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,  # Include package data specified in MANIFEST.in
)