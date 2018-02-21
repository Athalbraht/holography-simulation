from distutils.core import setup

setup(
    name='holopy',
    version='1.1b',
    packages=['Holopy', 'Holopy.Model', 'Holopy.tools', 'Holopy.Engine', 'Holopy.Webapp'],
    url='http://holography.ddns.net',
    license='MIT',
    author='Albert Szadziński',
    author_email='albert.szadzinski@protonmail.com',
    include_package_data=True,
    description='Program jest częścią pracy inżynierskiej pt. Klasyfikacja cyfrowych hologramów przy pomocy głębokich sieci neuronowych'
)
