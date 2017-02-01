

from collections import namedtuple


class EmModule(object):
    def __init__(self, cisco_em):
        self._cisco_em = cisco_em
        self._headers = cisco_em._headers
        self._url = cisco_em._url

    def _build(self, object_name, object_dict, display=None):
        display = display or object_name

        class ManagedObject(namedtuple(object_name, object_dict.keys())):
            _display = None

            def __str__(self):
                if not hasattr(self, self._display):
                    self._display = str(vars(self))
                else:
                    self._display = getattr(self, self._display)
                return str(self._display)

            def __repr__(self):
                return '<{} {}>'.format(
                    object_name,
                    self.__str__()
                )
        ManagedObject._display = display
        item = ManagedObject(**object_dict)
        return item