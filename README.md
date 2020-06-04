# PySpace

PySpace (working title) is an in-development programming-oriented space simulator. The eventual goal is to provide a sandbox environment to explore, mine, build, and fight along with other players. The project is still a long ways from completion, but is currently playable along with the client also hosted on this account.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run PySpace, you'll need the following

 - Python3.8
 - virtualenv
 - git

### Installing

In order to install a copy of the PySpace server, first clone the repository
and cd into it

```
$ git clone https://github.com/austinphilp/pyspace
$ cd pyspace
```

For a convenient installation and execution (until I get around to dockerizing the server), we've included a makefile with all the necessary logic included needed to perform the installation. First you'll want to create the virtual environment, then install pip dependencies. Both of these steps are contained in make recipes.

```
$ make venv
$ make install
```

And finally to run the server, simply use

```
$ make serve
```

## Running the tests

Pyspace has a comprehensive set of automated tests to ensure reliability. In
order to run them simply use the `test` make recipe.

```
$ make test
```

### Coding Style Tests

This project is PEP-8 compliant, in order to verify compliance, simply use the
following make recipe

```
make flake8
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Austin Philp** - *Initial work* - [AustinPhilp](https://github.com/austinphilp)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
