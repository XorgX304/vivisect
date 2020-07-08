# APIs for Windows 64-bit ntoskrnl library.
# Built as a delta from the 32-bit version.
# Format:  retval, rettype, callconv, exactname, arglist(type, name)
#          arglist type is one of ['int', 'void *']
#          arglist name is one of [None, 'funcptr', 'obj', 'ptr']

import vivisect.impapi.winkern.i386 as v_k_i386

apitypes = dict(v_k_i386.apitypes)

api = {}
for normname, (rtype, rname, cconv, cname, cargs) in v_k_i386.api.items():
    api[normname] = (rtype, rname, 'msx64call', cname, cargs)
