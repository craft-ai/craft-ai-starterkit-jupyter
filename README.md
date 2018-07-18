# **craft ai** Jupyter Notebook starter kit #

[![License](https://img.shields.io/badge/license-BSD--3--Clause-42358A.svg?style=flat-square)](LICENSE)

[**craft ai** _AI-as-a-service_](http://craft.ai) enables your services to learn every day: provide a personalized experience to each user and automate complex tasks.

This repository hosts a fully working application, in a **NYC taxi trip** context, integrating [**craft ai**](http://craft.ai) written in Python using [**craft ai** official Python client](https://pypi.python.org/pypi?:action=display&name=craft-ai).

The end goal: give an insight of the best New York city areas to find client as a taxi driver. Using **craft ai** to analyze the [2017 yellow taxi trip records](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml), this simple application learns when each NYC areas needs taxis.

## Setup ##

- Download or clone the [sources from GitHub](https://github.com/craft-ai/craft-ai-starterkit-notebook),
- Install [Python v3.5](https://www.python.org/downloads/) on your computer, alternatively install any version of Python and install [pyenv](https://github.com/pyenv/pyenv#installation),
- Install [pipenv](https://docs.pipenv.org/#install-pipenv-today) to properly manage dependencies,
- Install the dependencies including **craft ai** python client, by running `pipenv install` in the cloned or downloaded repository, from a terminal.
- in this directory, fill a `.env` file setting the following variable:
    - `CRAFT_TOKEN` allows you to [authenticate your calls to the **craft ai** API](https://beta.craft.ai/doc/python#1---retrieve-your-credentials):
    ```sh
    CRAFT_TOKEN=my-token
    ```

## Run ##

The following will:

1. create an agent by taxi zone,
2. add a bunch of context operations from the example dataset,
3. compute decision trees and
4. take a few decisions.

```sh
pipenv run start
```

### What do next ? ###


## About the dataset ##


### Data preparation ###

> The pre-treated data are already computed and available for this example.




> The **craft ai** user documentation can be found at <https://beta.craft.ai/doc> and technical questions can be sent by email at [support@craft.ai]('mailto:support@craft.ai').
