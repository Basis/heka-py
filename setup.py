import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.rst')) as f:
    README = f.read()


if 2 < sys.version_info.major:
    # Google protobuf doesn't support Python 3 outside beta:
    protobuf_library = 'protobuf==3.0.0b3'
else:
    protobuf_library = 'protobuf'


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['heka']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='heka-py',
    version='0.30.3',
    description="Metrics Logging",
    long_description=README,
    classifiers=[
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
    keywords='heka metrics logging client',
    author='Rob Miller',
    author_email='rmiller@mozilla.com',
    url='https://github.com/mozilla-services/heka-py',
    license='MPLv2.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        protobuf_library,
    ],
    tests_require=[
        'mock',
        'pytest',
    ],
    cmdclass={
        'test': PyTest
    },
)
