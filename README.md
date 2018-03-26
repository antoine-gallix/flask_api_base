# A simple flask service

Because we have to start somewhere.

## What is it?

A starting point to develop a flask API. Basic structure for application, test, logging, and config is there for you to fill with useful features.

## Setup

Start a new virtualenv with python 3 and install requirements:

    pip install -r requirements.txt

## Run Tests

    invoke tests

## Run Server Manually

    invoke run

Then attack the server on `localhost:5000`.

## Run Server In A Container

With docker installed:

    invoke build-image
    invoke run-image

Then test the same way as for the local server.
