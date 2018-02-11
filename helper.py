def bths(bytes_array): # bytes to hex string
    return "".join("%02x " % b for b in bytes_array[::-1])

def bths_ex(bytes_array): # without space
    return "".join("%02x" % b for b in bytes_array[::-1])
