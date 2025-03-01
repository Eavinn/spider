from setuptools import find_packages, setup

with open("VERSION.txt", 'r') as f:
    version = f.read().strip()


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='scrapy_plus',  # 模块名称
    version=version,
    description='A mini spider framework, like Scrapy',  # 描述
    packages=find_packages(exclude=[]),
    author='mengliang',
    author_email='mengliang.1992@163.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='#',
    install_requires=parse_requirements("requirements.txt"),  # 所需的运行环境
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
