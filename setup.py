from setuptools import setup

setup(
    name='slackbot',
    packages=['slackbot'],
    include_package_data=True,
    install_requires=[
        'flask',
        'dotenv',
        'slack-sdk'
    ],
)
