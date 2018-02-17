def bths(bytes_array): # bytes to hex string
    return "".join("%02x " % b for b in bytes_array[::-1])
