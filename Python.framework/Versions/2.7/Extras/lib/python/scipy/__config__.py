# This file is generated by /AppleInternal/BuildRoot/Library/Caches/com.apple.xbs/Binaries/python_modules/install/TempContent/Objects/2.7/scipy-0.13.0b1/setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

atlas_threads_info={}
blas_opt_info={'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)], 'extra_compile_args': ['-msse3', '-I/AppleInternal/BuildRoot/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.Internal.sdk/System/Library/Frameworks/vecLib.framework/Headers']}
openblas_info={}
umfpack_info={}
atlas_blas_threads_info={}
lapack_opt_info={'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)], 'extra_compile_args': ['-msse3']}
atlas_info={}
lapack_mkl_info={}
blas_mkl_info={}
atlas_blas_info={}
mkl_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    