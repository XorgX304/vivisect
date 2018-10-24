# APIs for Windows 64-bit ntoskrnl library.
# Built as a delta from the 32-bit version.
# Format:  retval, rettype, callconv, exactname, arglist(type, name)
#          arglist type is one of ['int', 'void *']
#          arglist name is one of [None, 'funcptr', 'obj', 'ptr']

# List the normalized name of any 32-bit functions to omit.
api_32_omits = []

# Define any functions specific to 64-bit.
api_64_adds = {
    }


# Build from the 32-bit API, skipping omits, changing the calling convention,
# and adding any specific 64-bit functions.
apitypes = {}
api = {}

import vivisect.impapi.winkern.i386 as m32
for name in m32.api.iterkeys():
    if name in api_32_omits:
        continue
    (rtype,rname,cconv,cname,cargs) = m32.api[name]
    api[name] = (rtype, rname, 'msx64call', cname, cargs)
api.update(api_64_adds)
