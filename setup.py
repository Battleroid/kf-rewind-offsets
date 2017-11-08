from setuptools import find_packages, setup
from pip.req import parse_requirements
from pip.download import PipSession

reqs = parse_requirements('requirements.txt', session=PipSession())
requirements = [str(req.req) for req in reqs]

setup(
    name='kf-rewind-offsets',
    author='Casey Weed',
    author_email='casey@caseyweed.com',
    description='Rewind or set offsets for a given consumer group',
    url='https://github.com/battleroid/kf-rewind-offsets',
    py_modules=['rewind'],
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        rewind-offsets=rewind:main
    """
)
