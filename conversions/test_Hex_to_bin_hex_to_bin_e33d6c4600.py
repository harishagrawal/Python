# Test generated by RoostGPT for test aa using AI Type Open AI and AI Model gpt-4

"""
1. Scenario: Test when a valid hexadecimal number is passed to the function.
- Description: The function should return the binary equivalent of the hexadecimal number.
- Input: "AC"
- Expected Output: 10101100

2. Scenario: Test when a hexadecimal number with leading and trailing whitespaces is passed to the function.
- Description: The function should ignore the whitespaces and return the binary equivalent of the hexadecimal number.
- Input: "   12f   "
- Expected Output: 100101111

3. Scenario: Test when a hexadecimal number with both upper and lower case letters is passed to the function.
- Description: The function should treat upper and lower case letters equally and return the binary equivalent of the hexadecimal number.
- Input: "FfFf"
- Expected Output: 1111111111111111

4. Scenario: Test when a negative hexadecimal number is passed to the function.
- Description: The function should return the negative binary equivalent of the hexadecimal number.
- Input: "-fFfF"
- Expected Output: -1111111111111111

5. Scenario: Test when an invalid hexadecimal number is passed to the function.
- Description: The function should raise a ValueError indicating that an invalid value was passed to the function.
- Input: "F-f"
- Expected Output: ValueError: Invalid value was passed to the function

6. Scenario: Test when an empty string is passed to the function.
- Description: The function should raise a ValueError indicating that no value was passed to the function.
- Input: ""
- Expected Output: ValueError: No value was passed to the function

7. Scenario: Test when a hexadecimal number with leading zeros is passed to the function.
- Description: The function should ignore the leading zeros and return the binary equivalent of the hexadecimal number.
- Input: "000AC"
- Expected Output: 10101100

8. Scenario: Test when a large hexadecimal number is passed to the function.
- Description: The function should return the binary equivalent of the large hexadecimal number.
- Input: "9A4FBCD1"
- Expected Output: 1001101010111110110011010001

"""
import pytest
import hex_to_bin

def test_valid_hexadecimal():
    assert hex_to_bin.hex_to_bin("AC") == 10101100

def test_whitespace_hexadecimal():
    assert hex_to_bin.hex_to_bin("   12f   ") == 100101111

def test_upper_and_lower_case_hexadecimal():
    assert hex_to_bin.hex_to_bin("FfFf") == 1111111111111111

def test_negative_hexadecimal():
    assert hex_to_bin.hex_to_bin("-fFfF") == -1111111111111111

def test_invalid_hexadecimal():
    with pytest.raises(ValueError) as e_info:
        hex_to_bin.hex_to_bin("F-f")
    assert str(e_info.value) == 'Invalid value was passed to the function'

def test_empty_hexadecimal():
    with pytest.raises(ValueError) as e_info:
        hex_to_bin.hex_to_bin("")
    assert str(e_info.value) == 'No value was passed to the function'

def test_leading_zeros_hexadecimal():
    assert hex_to_bin.hex_to_bin("000AC") == 10101100

def test_large_hexadecimal():
    assert hex_to_bin.hex_to_bin("9A4FBCD1") == 1001101010111110110011010001
