#!/usr/bin/python


def fmt_data_quantity(bytes, multiple=1024):
    try:
        if bytes < multiple * multiple:
            return "%dK" % ((bytes) / multiple)

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
    test = [1023, 1024, 1025, 1024 * 1023, 1024 *
            1024, 1024 * 1025, 1024 * 1024 * 1024 * 9]
    for data in test:
        print fmt_data_quantity(data)
