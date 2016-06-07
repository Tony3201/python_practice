#!/usr/bin/python
# coding:utf8


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def human_readable_data_quantity(quantity, multiple=1024):
    try:
        abs_quantity = abs(quantity)
        for unit in ['M', 'G', 'T', 'P', 'E', 'Z']:
            # if quantity < 10G, unit is M
            if abs_quantity < multiple * 10:
                return "%d%s" % (abs_quantity, unit)
            abs_quantity /= multiple

        return "%d%s" % (abs_quantity, 'Y')

    except TypeError:
        return '0M'


print human_readable_data_quantity('a')
print human_readable_data_quantity(20480)
print human_readable_data_quantity(20479)
print human_readable_data_quantity(-2)
print human_readable_data_quantity(19456)


# print sizeof_fmt('a')
print sizeof_fmt(20480)
print sizeof_fmt(20479)
print sizeof_fmt(-2)
print sizeof_fmt(19456)
