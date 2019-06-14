Additional badges
-----------------

When you see an input including the badge
[![with custom code](https://img.shields.io/badge/with-custom_code-red.svg)](),
you should consider that in order to run this input file you need a custom version of the
PLUMED code. The required code might be specified in the instructions associated to
this input file, or might have to be asked directly to the authors. This also implies
that this test should be expected to fail when tested on the official PLUMED versions.

When you see an input including the badge
[![with LOAD](https://img.shields.io/badge/with-LOAD-yellow.svg)](),
you should consider that this input file uses the `LOAD` action, which in turn
compiles on the fly some code that is provided along with the input file.
This means that this input file uses some source code that is not included in the
official PLUMED distribution and might be thus less documented and less tested.
