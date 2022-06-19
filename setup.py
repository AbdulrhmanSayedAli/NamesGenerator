from setuptools import find_packages, setup
setup(
    name='NamesGeneratorByRoctes7',
    packages=find_packages(include=['NamesGeneratorByRoctes7']),
    version='1.0.4',
    description='you can draw your name into the console in a beautiful way',
    author='Abdulrhman Sayed Ali',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)