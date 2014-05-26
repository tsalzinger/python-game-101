__author__ = 'Thomas Scheinecker'


class StringUtil(object):
    @staticmethod
    def dict_to_str(dict_):
        to_str = '{'
        items = []
        for key, value in dict_.items():
            items.append('{key}: {value}'.format(**{'key': key, 'value': value}))
        to_str += ', '.join(items)
        to_str += '}'
        return to_str
