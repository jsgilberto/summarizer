# Summarizer

## Description

Small web app exposing a Machine Learning model from HuggingFace. 
The model creates summaries of text.

## Requirements

This web app server was built with python 3.6 and depends on the following
packages:

```sh
flask==1.1.2
flask-restful==0.3.8
transformers==4.5.0
torch==1.8.1+cpu
torchvision==0.9.1+cpu
torchaudio==0.8.1
sentencepiece==0.1.95
protobuf==3.15.8
pytest==6.2.3
flake8==3.9.0
flake8-docstrings==1.6.0
pep8-naming==0.11.1
mypy==0.812
```

In order to install all the dependencies execute the following command in your
terminal:

```sh
$ pip install -r requirements.txt --find-links https://download.pytorch.org/whl/torch_stable.html
```

It's recommended that you use a virtual environment, ie. virtualenv, venv, etc.

## What to expect

This web app is only intended for demo purposes. It uses Flask for the web app
and transformers for the Machine Learning model.

The model is a summarization transformer from HuggingFace, and its exposed at 
`POST http://127.0.0.1:5000/api/predict`.

## How to use it

First clone the project to your local computer:

```sh
$ git clone https://github.com/jsgilberto/summarizer.git
```

To start the web app, execute the following command:

```sh
$ python3 src/app.py
```

By default, the app is going to run on port 5000.

To start making predictions, make a POST request to the following endpoint:

```sh
$ curl --location --request POST 'http://127.0.0.1:5000/api/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "As they rounded a bend in the path that ran beside the river..."
}'
```

Make sure the text is long enough for the model so it is be able to make a
summary. If its not long enough, it will return as a response the same text you
initially passed.

## Type consistency

I used mypy for type consistency with the configuration provided in `mypy.ini`

If you want to check type consistency, execute the following command:

```sh
$ mypy src
```

## Code validation (PEP-8)

flake8 is the tool used in this module. For validating the code, the following 
command is used:

```sh
$ flake8
```

It uses the `.flake8` configuration file placed in the root of the project.

## Tests

For testing `pytest` was the choice. The tests are located in the `tests` folder
placed in the root of this project.

```sh
$ python3 -m pytest -W ignore::DeprecationWarning
```

or:

```sh
$ pytest -W ignore::DeprecationWarning
```

The tests are only an example of what it would look like in a real world project.

## Deployment

For this project I decided to use a WSGI application server: `Gunicorn`. This helps
us to keep multiple processes of the flask application running.

The following command was used to run gunicorn:

```sh
gunicorn -w 4 -b 127.0.0.1:8000 --chdir $(pwd)/src wsgi:app 
```

## Suggestions

Please feel free to make any suggestions on the project.
