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
set -g PYTHONPATH=(pwd)/lib/python3.12/site-packages
```

Note that if *fish* is called from within bash/zsh the `PYTHONPATH` variable
needs to be set in the parent shell.

## Editor

If neovim is used install the following packages:

* pylsp
* mypy
* isort

The pyright package 
