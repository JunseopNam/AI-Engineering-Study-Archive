# q02 진법 바꾸기

octo = 0o177
hexa = 0xABC
integer = 255
string_hexa = "ff"
string_octo = "0o34"

print(octo, hexa)
print(bin(integer), oct(integer), hex(integer))
print(int(string_hexa, 16), int(string_octo, 8))