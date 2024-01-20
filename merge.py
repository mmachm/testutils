from typing import Dict, Union, List, Tuple

sentinel = object()


def merge(
        object_with_any, actual_object, *args
):
    """
    Intended usage: self.assertEqual(*merge(expected_result, actual_result, message))

    :param object_with_any:
    :param actual_object:
    :param args:
    :return:
    """
    return (_merge_objects(object_with_any, actual_object), actual_object) + args


def _merge_objects(object_with_any, actual_object):
    if object_with_any == actual_object:
        return actual_object

    elif(
        isinstance(object_with_any, dict)
        and isinstance(actual_object, dict)
    ):
        for key, value in object_with_any.items():
            actual_value = actual_object.get(key, sentinel)
            if actual_value is not sentinel:
                object_with_any[key] = _merge_objects(value, actual_value)

    elif(
        isinstance(object_with_any, list)
        and isinstance(actual_object, list)
        and len(actual_object) == len(object_with_any)
    ):
        for index, item in enumerate(object_with_any):
            actual_item = actual_object[index]
            object_with_any[index] = _merge_objects(item, actual_item)

    return object_with_any
