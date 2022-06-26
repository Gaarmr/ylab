def int32_to_ip(int32):
    parts = (
        (int32 >> 24) & 0xFF,
        (int32 >> 16) & 0xFF,
        (int32 >>  8) & 0xFF,
        (int32 >>  0) & 0xFF,
    )
    return '.'.join(str(x) for x in parts)


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
