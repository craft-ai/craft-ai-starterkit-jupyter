# **craft ai** Jupyter Notebook starter kit #

[![Build Status](https://img.shields.io/travis/craft-ai/craft-ai-starterkit-jupyter/master.svg?style=flat-square)](https://travis-ci.org/craft-ai/craft-ai-starterkit-jupyter) [![License](https://img.shields.io/badge/license-BSD--3--Clause-42358A.svg?style=flat-square)](LICENSE)

[**craft ai** API](http://craft.ai) leverages explainable Artificial Intelligence to 10x your knowledge workers productivity. craft ai is the first high level AI API enabling Automated Machine Learning at the individual level that generates explainable predictive models on the fly.

This repository hosts a fully working notebook, in a **NYC taxi trip** context, integrating [**craft ai**](http://craft.ai) written with Jupyter using [**craft ai** official Python client](https://pypi.python.org/pypi?:action=display&name=craft-ai).

The end goal: give an insight of the best New York city areas to find clients as a taxi driver. Using **craft ai** to analyze the [2017 yellow taxi trip records](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml), this simple application learns when each NYC areas needs taxis.

## Setup ##

- Download or clone the [sources from GitHub](https://github.com/craft-ai/craft-ai-starterkit-jupyter),
- Install [Python v3.7](https://www.python.org/downloads/) on your computer, alternatively install any version of Python and install [pyenv](https://github.com/pyenv/pyenv#installation),
- Install [pipenv](https://docs.pipenv.org/#install-pipenv-today) to properly manage dependencies,
- Install the dependencies including **craft ai** python client, by running `pipenv install` in the cloned or downloaded repository, from a terminal.
- Create a project following the subsection 1 of this [tutorial](https://beta.craft.ai/doc/python#1---retrieve-your-credentials) and copy the write token
- in this directory, fill a `.env` file setting the following variable:
    - `CRAFT_TOKEN` allows you to [authenticate your calls to the **craft ai** API](https://beta.craft.ai/doc/python#1---retrieve-your-credentials) :
    ```sh
    CRAFT_TOKEN=paste-your-token-here
    ```

## Run ##

The following command will allow the user to access three notebooks: `Preprocessing.ipynb`, `Main.ipynb` and `Benchmarks.ipynb`. We recommend to start by running `Main.ipynb`.

```sh
pipenv run notebook
```

* The principal work is done in `Main.ipynb`.
* `Preprocessing.ipynb` has been written to generate the dataset `yellow.csv`
* `Benchmarks.ipynb` allows the user to have a insight the Craft AI's agents performances.

### What do next ? ###
You can use this use case as a `craftai.pandas` example, and start your own projects with the tools provided by the library.

## About the dataset ##
The work is based on the dataset `yellow.csv` located in the directory _data/_. (It is possible to regenerate this dataset by using the notebook `Preprocessing.ipynb`.)

`yellow.csv` has been extracted from the data available on the ___NYC Taxi and Limousine Commission (LTC)___ [webpage](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml).

> The **craft ai** user documentation can be found at <https://beta.craft.ai/doc> and technical questions can be sent by email at [support@craft.ai]('mailto:support@craft.ai').
