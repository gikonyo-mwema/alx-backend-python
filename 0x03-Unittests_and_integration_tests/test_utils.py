#!/usr/bin/env python3
"""
Test module for utils.access_nested_map, utils.get_json, and utils.memoize
functions.
"""

import unittest
from typing import Dict, Tuple, Union, Any, Type
from unittest.mock import patch, Mock
from parameterized import parameterized # type: ignore
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str, ...],
            expected: Union[Dict[str, Any], int]
    ) -> None:
        """
        Test that access_nested_map returns the correct value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str, ...],
            exception: Type[BaseException]
    ) -> None:
        """
        Test that access_nested_map raises KeyError for invalid paths
        and checks the exception message.
        """
        with self.assertRaises(exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"KeyError('{path[-1]}')")


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test that get_json returns the expected result and that the mocked
        get method was called exactly once.
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator
    """

    def test_memoize(self) -> None:
        """
        Test that a method decorated with memoize caches the result and
        calls the underlying method only once.
        """
        class TestClass:
            """
            Test class to demonstrate memoize functionality.
            """

            def a_method(self) -> int:
                """
                Method that returns a constant value.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                Property method that calls a_method.
                """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test_class = TestClass()
            
            # First call to a_property should invoke a_method
            result_first_call = test_class.a_property()
            self.assertEqual(result_first_call, 42)
            
            # Second call to a_property should return the cached result
            result_second_call = test_class.a_property()
            self.assertEqual(result_second_call, 42)
            
            # Ensure that a_method was called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
