#!/usr/bin/python


def fmt_data_quantity(bytes, multiple=1024):
    try:
        if bytes < multiple * multiple:
            return "%dB" % (bytes)

        quantity = bytes / multiple / multiple
        for unit in ['M', 'G', 'T', 'P', 'E', 'Z']:
            # if quantity < 10G, unit is M
            if quantity < multiple * 10:
                return "%d%s" % (quantity, unit)
            quantity /= multiple

        return "%d%s" % (quantity, 'Y')

    except TypeError:
        return '0M'


if __name__ == '__main__':
    print fmt_data_quantity(1024 * 1025)
