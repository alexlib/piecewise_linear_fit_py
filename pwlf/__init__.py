from .pwlf import PiecewiseLinFit
from .pwlf import PiecewiseLinFitTF
import os

# add rudimentary version tracking
VERSION_FILE = os.path.join(os.path.dirname(__file__), 'VERSION')
__version__ = open(VERSION_FILE).read().strip()
