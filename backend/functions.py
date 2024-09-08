import ctypes
import os

base_dir = os.path.dirname(__file__)
dll_path = os.path.join(base_dir, 'ccvalidator.dll')
dll = ctypes.CDLL(dll_path)


# Define the function prototypes
# For `sumOddDigits` and `sumEvenDigits`, return type is int, and argument type is c_char_p (C-style string)
dll.sumOddDigits.restype = ctypes.c_int
dll.sumOddDigits.argtypes = [ctypes.c_char_p]

dll.sumEvenDigits.restype = ctypes.c_int
dll.sumEvenDigits.argtypes = [ctypes.c_char_p]

# For `cardIsValid`, return type is bool (using ctypes.c_bool), and argument type is c_char_p (C-style string)
dll.cardIsValid.restype = ctypes.c_int
dll.cardIsValid.argtypes = [ctypes.c_char_p]

# Example usage
  # Note the 'b' prefix to indicate a byte string

# Call the functions
def cardIsValid(str):
    card_number = str.encode('utf-8')
    sum_odd = dll.sumOddDigits(card_number)
    sum_even = dll.sumEvenDigits(card_number)
    is_valid = dll.cardIsValid(card_number)

    print(f"Sum of odd digits: {sum_odd}")
    print(f"Sum of even digits: {sum_even}")
    print(f"Card is valid: {bool(is_valid)}")
    return bool(is_valid)

if __name__ == '__main__':
    cardIsValid('6011000990139424')
