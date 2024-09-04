# ********RoostGPT********
"""
Test generated by RoostGPT for test demoPythonTest using AI Type  and AI Model 

ROOST_METHOD_HASH=equilibrium_index_ca20307e48
ROOST_METHOD_SIG_HASH=equilibrium_index_56f613271b


Scenario 1: Testing equilibrium index in a normal case
Details:
  TestName: test_equilibrium_index_normal
  Description: This test verifies if the function correctly identifies the equilibrium index in a given array under normal circumstances.
Execution:
  Arrange: We need an array of integers where an equilibrium index exists.
  Act: Call the equilibrium_index function and pass the prepared array.
  Assert: Check if the returned index is the correct equilibrium index.
Validation:
  This test is important because it checks the primary functionality of the equilibrium_index function. The expected result is the correct equilibrium index which is a crucial part of the function's specifications.

Scenario 2: Testing equilibrium index in a case where no equilibrium index exists
Details:
  TestName: test_equilibrium_index_no_exists
  Description: This test verifies if the function correctly returns -1 when there is no equilibrium index in a given array.
Execution:
  Arrange: We need an array of integers where no equilibrium index exists.
  Act: Call the equilibrium_index function and pass the prepared array.
  Assert: Check if the returned value is -1.
Validation:
  This test is important because it checks the function's ability to handle cases where no equilibrium index exists. The expected result is -1 which aligns with the function's specifications.

Scenario 3: Testing equilibrium index in a case where all elements in the array are equal
Details:
  TestName: test_equilibrium_index_all_equal
  Description: This test verifies if the function correctly identifies the equilibrium index when all elements in the array are equal.
Execution:
  Arrange: We need an array of integers where all elements are equal.
  Act: Call the equilibrium_index function and pass the prepared array.
  Assert: Check if the returned index is the correct equilibrium index.
Validation:
  This test is important because it checks the function's ability to handle special cases where all elements in the array are equal. The expected result is the correct equilibrium index which is a crucial part of the function's specifications.

Scenario 4: Testing equilibrium index in a case where the array is empty
Details:
  TestName: test_equilibrium_index_empty_array
  Description: This test verifies if the function correctly returns -1 when the array is empty.
Execution:
  Arrange: We need an empty array.
  Act: Call the equilibrium_index function and pass the empty array.
  Assert: Check if the returned value is -1.
Validation:
  This test is important because it checks the function's ability to handle edge cases where the array is empty. The expected result is -1 which aligns with the function's specifications.
"""

# ********RoostGPT********
import pytest
from arrays.equilibrium_index_in_array import equilibrium_index

class Test_EquilibriumIndexInArrayEquilibriumIndex:

    def test_equilibrium_index_normal(self):
        arr = [-7, 1, 5, 2, -4, 3, 0]
        result = equilibrium_index(arr)
        assert result == 3, "Equilibrium index under normal circumstances is not correct."

    def test_equilibrium_index_no_exists(self):
        arr = [1, 2, 3, 4, 5]
        result = equilibrium_index(arr)
        assert result == -1, "Function does not return -1 when no equilibrium index exists."

    def test_equilibrium_index_all_equal(self):
        arr = [1, 1, 1, 1, 1]
        result = equilibrium_index(arr)
        assert result == 2, "Equilibrium index when all elements in the array are equal is not correct."

    def test_equilibrium_index_empty_array(self):
        arr = []
        result = equilibrium_index(arr)
        assert result == -1, "Function does not return -1 when the array is empty."
