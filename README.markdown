# Code exercises and experiments


## Tutorials

(Arcade)[https://learn.arcade.academy/en/latest/chapters/14_advanced_looping/advanced_looping.html]


## Environment 


### Virtual environment

Create a python virtual environment with the command

```sh
python3 -m venv <project name>
```

To have python language servers work in neovim with virtual env
set `PYTHONPATH` to <virtual env fodler>/lib/<python version>/site-packages`.

Shell:

```sh
export PYTHONPATH=`pwd`/lib/python3.12/site-packages
```
Fish:

```sh
set -gx PYTHONPATH (pwd)/lib/python3.12/site-packages
```
* *g* = global
* *x* = child processes (e.g. vim)

## Editor

If neovim is used install the following packages:

* pylsp
* mypy
* isort

