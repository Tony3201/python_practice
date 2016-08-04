#!/usr/bin/python


def fmt_data_quantity(quantity, multiple=1024):
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

if __name__ == '__main__':
    print fmt_data_quantity(715)
    print fmt_data_quantity(2014)
