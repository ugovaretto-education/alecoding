# import sys
# additional_directory = r"."
# sys.path.append(additional_directory)
# # the 'r' prefix marks the string as a raw string with no
# # escape sequences, a single backslash is interpreted as a
# # single backslash instead of requiring two unless is the
# # last characted in the string

import mroot
import mroot.child1 as c1
import mroot.child2 as c2

mroot.root_fun()
c1.child1_fun()
c2.child2_fun()

c1.child1_invoke_root()
c1.child1_invoke_child2()

# mroot.missing_child.not_reachable()
# from mroot import *
#
# child1.child1_fun()
# child2.child2_fun()
# root_fun()
