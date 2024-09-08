#include <cmath>
#include <cstring>

extern "C" {
    __declspec(dllexport) int sumOddDigits(const char* cardNumber) {
        int sum = 0;
        int len = strlen(cardNumber);  // Use strlen to get the length of the C-style string

        for (int i = 1; i < len; i += 2) {
            sum += (cardNumber[i] - '0');
        }
        return sum;
    }

    __declspec(dllexport) int sumEvenDigits(const char* cardNumber) {
        int sum = 0;
        int len = strlen(cardNumber);  // Use strlen to get the length of the C-style string

        for (int i = 0; i < len; i += 2) {
            int digit = (cardNumber[i] - '0') * 2;
            float check = digit / 10.0f;
            if (check >= 1) {
                int digit1 = static_cast<int>(floor(check));
                int digit2 = digit % 10;
                sum += digit1 + digit2;
            } else {
                sum += digit;
            }
        }
        return sum;
    }

    __declspec(dllexport) int cardIsValid(const char* cardNumber) {
        int result = 0;
        result += sumOddDigits(cardNumber) + sumEvenDigits(cardNumber);
        
        return result % 10 == 0;
    }
}


