import re


_first_camel_case_regex = re.compile('(.)([A-Z][^A-Z]+)')
_second_camel_case_regex = re.compile('([^A-Z_])([A-Z])')


def to_camel_case(snake_case_string):
    """
    Convert a string from snake case to camel case.

    :param snake_case_string: Snake-cased string to convert to camel case.
    :returns: Camel-cased version of snake_case_string.
    """
    parts = snake_case_string.split('_')
    return parts[0] + ''.join([i.title() for i in parts[1:]])


def to_snake_case(camel_case_string):
    """
    Convert a string from camel case to snake case.

    :param camel_case_string: Camel-cased string to convert to snake case.
    :return: Snake-cased version of camel_case_string.
    """
    first_pass = _first_camel_case_regex.sub(r'\1_\2', camel_case_string)
    return _second_camel_case_regex.sub(r'\1_\2', first_pass).lower()
