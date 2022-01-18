from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='spotify-museum',
    version='1.1',
    packages=find_packages(),
    url='https://github.com/joshbasims/spotify-museum',
    license='',
    author='joshbasims',
    author_email='joshbasims@gmail.com',
    description='Save the last 2 Discovery Weekly Playlists from Spotify'
)
