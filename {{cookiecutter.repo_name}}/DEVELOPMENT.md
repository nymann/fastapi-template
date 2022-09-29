### Cross platform development

By installing `make` you can do the following:

```sh
$ make help
make install
 - Installs {{cookiecutter.package_name}}.
make install-all
 - Install {{cookiecutter.package_name}}, all development and tests dependencies.
make test
 - Runs integration tests and unit tests
make unit-test
 - Runs integration tests
make integration-tests
 - Runs unit tests
make lint
 - Lints your code (black, flake8 and mypy).
make fix
 - Autofixes imports and some formatting.
```

### Developing on Linux

#### Run helping tools automatically on file change

While the `make` targets is an okay way to run things, I find it helpful to have my tests and linter running in separate terminal windows to get continous quick feedback.

The command `ag` is from The Silver Searcher program which can be found [here](https://archlinux.org/packages/community/x86_64/the_silver_searcher/). And the `entr` program can be found [here](https://archlinux.org/packages/community/x86_64/entr/).

###### Run `unit tests` on file change automatically

```sh
alias unit="ag -l | entr -c pytest --durations=0 tests/unit_tests"
```

###### Run `flake8` on file change automatically

```sh
alias flakeit="ag -l | entr -c flake8 tests src"
```
