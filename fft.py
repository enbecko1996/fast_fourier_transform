import numpy as np

the_data = [1, 3, 4, 2, -1, 9, 2, 7]


def do_fft_on(data):
    data = pad_data(data)


def pad_data(data):
    data_len = len(data)
    if is_power_of_2(data_len):
        return data
    else:
        i = 1
        while data_len > 0:
            i <<= 1
            data_len >>= 1
        data.extend(np.zeros(i - len(data)))
        return data


def is_power_of_2(num):
    return ((num & (num - 1)) == 0) and num != 0


