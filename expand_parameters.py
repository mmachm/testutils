import sys
import warnings
from functools import wraps
from typing import List

from parameterized.parameterized import default_doc_func, default_name_func, delete_patches_if_need, parameterized, \
    reapply_patches_if_need, skip_on_empty_helper


def expand_parameters(test_input: List, name_func=None, doc_func=None, skip_on_empty=False, default_input_index=0, **legacy):
    def decorator(f):
        _expand(test_input, name_func, doc_func, skip_on_empty, **legacy)(f)
        default_parameters = parameterized.input_as_callable((test_input[default_input_index],))()[0]
        return parameterized.param_as_standalone_func(default_parameters, f, f.__name__)

    return decorator


def _expand(_input, name_func=None, doc_func=None, skip_on_empty=False,
           **legacy):
    """
    Reference: Code taken almost verbatim from parameterized.expand v0.8.1
    Only minor changes made.

    https://pypi.org/project/parameterized/

    A "brute force" method of parameterizing test cases. Creates new
    test cases (which wrap the SAME old function, which never gets copied,
    the new parameters are being kept in a closure - and injects them
    into the namespace that the wrapped function is being defined in.
    Useful for parameterizing tests in subclasses of 'UnitTest',
    where Nose test generators don't work.
    """

    if "testcase_func_name" in legacy:
        warnings.warn("testcase_func_name= is deprecated; use name_func=",
                      DeprecationWarning, stacklevel=2)
        if not name_func:
            name_func = legacy["testcase_func_name"]

    if "testcase_func_doc" in legacy:
        warnings.warn("testcase_func_doc= is deprecated; use doc_func=",
                      DeprecationWarning, stacklevel=2)
        if not doc_func:
            doc_func = legacy["testcase_func_doc"]

    doc_func = doc_func or default_doc_func
    name_func = name_func or default_name_func

    def parameterized_expand_wrapper(f, instance=None):
        frame_locals = (sys._getframe(1) if hasattr(sys, "_getframe") else None).f_back.f_locals

        try:
            parameters = parameterized.input_as_callable(_input)()
        except:
            print()

        if not parameters:
            if not skip_on_empty:
                raise ValueError(
                    "Parameters iterable is empty (hint: use "
                    "`parameterized.expand([], skip_on_empty=True)` to skip "
                    "this test when the input is empty)"
                )
            return wraps(f)(skip_on_empty_helper)

        digits = len(str(len(parameters) - 1))
        for num, p in enumerate(parameters):
            name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)
            # If the original function has patches applied by 'mock.patch',
            # re-construct all patches on the just former decoration layer
            # of param_as_standalone_func so as not to share
            # patch objects between new functions
            nf = reapply_patches_if_need(f)
            frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
            frame_locals[name].__doc__ = doc_func(f, num, p)

        # Delete original patches to prevent new function from evaluating
        # original patching object as well as re-constructed patches.
        delete_patches_if_need(f)

        f.__test__ = False

    return parameterized_expand_wrapper
