# Test generated by RoostGPT for test aa using AI Type Open AI and AI Model gpt-4

"""
1. Scenario: Conversion from one unit to the same unit
    - Given: the value is 5, the from_type is "litre", and the to_type is "litre"
    - Expect: the function returns 5

2. Scenario: Conversion from cubic meters to litres
    - Given: the value is 1, the from_type is "cubic meter", and the to_type is "litre"
    - Expect: the function returns 1000

3. Scenario: Conversion from gallons to cubic yards
    - Given: the value is 1, the from_type is "gallon", and the to_type is "cubic yard"
    - Expect: the function returns approximately 0.00595 

4. Scenario: Conversion from cubic yards to litres
    - Given: the value is 1, the from_type is "cubic yard", and the to_type is "litre"
    - Expect: the function returns approximately 764.5549

5. Scenario: Conversion from cubic feet to cups
    - Given: the value is 1, the from_type is "cubic foot", and the to_type is "cup"
    - Expect: the function returns approximately 119.68831

6. Scenario: Conversion from cups to kilolitres
    - Given: the value is 10000, the from_type is "cup", and the to_type is "kilolitre"
    - Expect: the function returns approximately 2.365882

7. Scenario: Invalid 'from_type' value
    - Given: the value is 1, the from_type is "wrongUnit", and the to_type is "litre"
    - Expect: the function throws a ValueError with a message about the invalid 'from_type' value

8. Scenario: Invalid 'to_type' value
    - Given: the value is 1, the from_type is "litre", and the to_type is "wrongUnit"
    - Expect: the function throws a ValueError with a message about the invalid 'to_type' value

9. Scenario: Conversion from kilolitres to cubic meters
    - Given: the value is 1, the from_type is "kilolitre", and the to_type is "cubic meter"
    - Expect: the function returns 1

10. Scenario: Conversion from litres to gallons
    - Given: the value is 1, the from_type is "litre", and the to_type is "gallon"
    - Expect: the function returns approximately 0.264172

"""
import pytest
import volume_conversions

def test_volume_conversion_same_unit():
    assert volume_conversions.volume_conversion(5, "litre", "litre") == 5

def test_volume_conversion_cubic_metres_to_litres():
    assert volume_conversions.volume_conversion(1, "cubic meter", "litre") == 1000

def test_volume_conversion_gallons_to_cubic_yards():
    assert pytest.approx(volume_conversions.volume_conversion(1, "gallon", "cubic yard"), 0.00595)

def test_volume_conversion_cubic_yards_to_litres():
    assert pytest.approx(volume_conversions.volume_conversion(1, "cubic yard", "litre"), 764.5549)

def test_volume_conversion_cubic_feet_to_cups():
    assert pytest.approx(volume_conversions.volume_conversion(1, "cubic foot", "cup"), 119.68831)

def test_volume_conversion_cups_to_kilolitres():
    assert pytest.approx(volume_conversions.volume_conversion(10000, "cup", "kilolitre"), 2.365882)

def test_volume_conversion_invalid_from_type():
    with pytest.raises(ValueError, match="Invalid 'from_type' value: 'wrongUnit'"):
        volume_conversions.volume_conversion(1, "wrongUnit", "litre")

def test_volume_conversion_invalid_to_type():
    with pytest.raises(ValueError, match="Invalid 'to_type' value: 'wrongUnit'"):
        volume_conversions.volume_conversion(1, "litre", "wrongUnit")

def test_volume_conversion_kilolitres_to_cubic_metres():
    assert volume_conversions.volume_conversion(1, "kilolitre", "cubic meter") == 1

def test_volume_conversion_litres_to_gallons():
    assert pytest.approx(volume_conversions.volume_conversion(1, "litre", "gallon"), 0.264172)
