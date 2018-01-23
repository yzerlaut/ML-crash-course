def function_to_load_data(filename):
    # simple reading of binary
    return np.fromfile(filename, dtype='float32')
