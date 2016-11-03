"""Stubs for the binascii module."""

def a2b_base64(string: str) -> str: ...
def a2b_hex(hexstr: str) -> str: ...
def a2b_hqx(string: str) -> str: ...
def a2b_qp(string: str, header: bool = ...) -> str: ...
def a2b_uu(string: str) -> str: ...
def b2a_base64(data: str) -> str: ...
def b2a_hex(data: str) -> str: ...
def b2a_hqx(data: str) -> str: ...
def b2a_qp(data: str, quotetabs: bool = ..., istext: bool = ..., header: bool = ...) -> str: ...
def b2a_uu(data: str) -> str: ...
def crc32(data: str, crc: int = None) -> int: ...
def crc_hqx(data: str, oldcrc: int) -> int: ...
def hexlify(data: str) -> str: ...
def rlecode_hqx(data: str) -> str: ...
def rledecode_hqx(data: str) -> str: ...
def unhexlify(hexstr: str) -> str: ...

class Error(Exception): ...
class Incomplete(Exception): ...
