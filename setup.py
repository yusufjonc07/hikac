from setuptools import find_packages, setup

setup(
    name='hikvision_ac_python',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
       'starlette',
    ],
    author='Yusufjon Axmedov',
    author_email='yahmedov64@gmail.com',
    description='This modest python package helps you to get events from HIKVISION AC terminals.',
    long_description=open('./app/README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yusujonc07/hikvision-ac-python',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires=">=3.8"
)
