import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="handybelt",
    version="0.0.1",
    author="Charles Kawczynski",
    author_email="kawczynski.charles@gmail.com",
    description="A collection of functions I've found useful over the years.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charleskawczynski/handybelt",
    # packages=setuptools.find_packages(),
    # packages=[
    # 'handybelt',
    # 'screenshot',
    # 'getimage',
    # 'crop',
    # ],
    # package_dir={
    # 'handybelt': 'handybelt/handybelt',
    # 'screenshot': 'src/screenshot',
    # 'getimage': 'src/getimage',
    # 'crop': 'src/crop',
    # },
    # entry_points={
    #     'console_scripts': ['screenshot=screenshot.screenshot:main'],
    # },
    install_requires=[
          # 'markdown',
      ],
    scripts=['bin/screenshot.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)