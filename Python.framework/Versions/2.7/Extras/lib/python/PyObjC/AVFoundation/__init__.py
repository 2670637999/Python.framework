'''
Python mapping for the AVFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc

__bundle__ = _objc.initFrameworkWrapper("AVFoundation",
    frameworkIdentifier="com.apple.AVFoundation",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/AVFoundation.framework"),
    globals=globals())
