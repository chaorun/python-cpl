import os
import sys

from version import version as __version__
from version import author as __author__
from version import email as __email__
from version import license_ as __license__
from version import doc as __doc__

from recipes import Recipe, RecipeCrash
from parameters import Parameter
from frames import FrameConfig
from result import Result, CplError
from log import msg, lib_version
import dfs
import esorex

msg.domain = os.path.basename(sys.argv[0])
msg.level = msg.OFF

Recipe.dir = '.'
