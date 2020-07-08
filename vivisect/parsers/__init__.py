
"""
The vivisect.parsers package contains all the known file format parsers
for vivisect.  Each parser module must implement the following functions:

    parseFile(workspace, filename):
        Load the file into the given workspace
    parseBytes(workspace, bytes):
        Load the file (pre-read in) into the workspace

"""
# Some parser utilities

import md5
import sys
import struct

import vstruct.defs.macho as vs_macho

from vivisect.parsers.utils import md5File
from vivisect.parsers.utils import md5Bytes
from vivisect.parsers.utils import guessFormat
from vivisect.parsers.utils import guessFormatFilename


def getParserModule(fmt):
    # wb: we use the import statement here so that pyinstaller
    # will pick up the potential dependency.
    if fmt == "pe":
        import  vivisect.parsers.parse_pe
        return vivisect.parsers.parse_pe
    elif fmt == "blob":
        import vivisect.parsers.blob
        return vivisect.parsers.blob
    elif fmt == "elf":
        import vivisect.parsers.elf
        return vivisect.parsers.elf
    elif fmt == "ihex":
        import vivisect.parsers.ihex
        return vivisect.parsers.ihex
    elif fmt == "macho":
        import vivisect.parsers.macho
        return vivisect.parsers.macho

    mname = "%s" % fmt
    mod = sys.modules.get(mname)
    if mod == None:
        __import__(mname)
        mod = sys.modules[mname]
    return mod

