def int32_to_ip(int32):
    return '.'.join(str(x) for x in int32.to_bytes(4, byteorder='big'))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
