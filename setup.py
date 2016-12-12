from distutils.core import setup

setup(
    name='acp_direct_cherenkov',
    version='0.0.1',
    description='Mass production of airshowers using CORSIKA',
    url='https://github.com/thebiglebowsky/direct_cherenkov.git',
    author='Axel Arbet-Engels, Sebastian Achim Mueller',
    author_email='aaxel@student.ethz.ch',
    license='MIT',
    packages=[
        'acp_direct_cherenkov',
    ],
    package_data={'acp_direct_cherenkov': ['resources/*']},
    install_requires=[
        'docopt',
    ],
    entry_points={'console_scripts': [
        'acp_direct_cherenkov = acp_direct_cherenkov.main:main',
    ]},
    zip_safe=False,
)
