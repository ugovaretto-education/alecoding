# Python packages

To create a package:

1. Create directory
2. Create file `__init__.py` in directory
3. Create python files in directory
4. In `__init__.py` import the entire file/module or the symbols needed prefixing the name with '`.`'


To create sub-packages:

Repeat the above process inside the root directory of the main package.

Each subpackage can be accessed with the fully qualified name of the path to the
subpackage, e.g. `root.child1.child1_1`.

## `from package import *`

In the `__init__.py` file is possible to add an `__all__` list containing
the names of the subpackages and symbols to be exported when the client
code uses a `from package import *` statemement.
