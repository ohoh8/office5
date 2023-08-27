from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=g-bad-import-order
from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import

from tensorflow.python.util.lazy_loader import LazyLoader
contrib = LazyLoader('contrib', globals(), 'tensorflow.contrib')
del LazyLoader

from tensorflow.python.platform import flags  # pylint: disable=g-import-not-at-top
from tensorflow.python.platform import app  # pylint: disable=g-import-not-at-top
app.flags = flags

del absolute_import
del division
del print_function

# These symbols appear because we import the python package which
# in turn imports from tensorflow.core and tensorflow.python. They
# must come from this module. So python adds these symbols for the
# resolution to succeed.
# pylint: disable=undefined-variable
del python
del core
# pylint: enable=undefined-variable
