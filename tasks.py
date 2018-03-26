from invoke import task
from pathlib import Path
import os


@task
def tests(ctx):
    """run tests"""
    # add project to python path for the tests to be able to import the app.
    here = Path(__file__).resolve().parent
    os.environ['PYTHONPATH'] = str(here)
    command = 'py.test'
    print('run test suite')
    ctx.run(command)


@task
def run(ctx, config='dev'):
    """run the application
    config : ['prod','dev']
    """
    print('run test suite in {} mode'.format(config))
    # if the following import is called before installing requirements,
    # it would crash the file
    from service import create_app
    app = create_app()
    if config == 'prod':
        app.run(host='0.0.0.0')
    elif config == 'dev':
        app.run(debug=True)


@task
def build_image(ctx, name='caps_proxy', version='dev'):
    """build docker image"""

    command = 'docker build -t {}:{} .'.format(name, version)
    ctx.run(command)


@task
def run_image(ctx, name='caps_proxy', version='dev'):
    """run docker image"""

    command = 'docker run --rm -p 5000:5000 {}:{}'.format(name, version)
    ctx.run(command)
