#!/usr/bin/env python3
"""
Test module for utils.access_nested_map function
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises KeyError for invalid paths
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json function
    """

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """
        Test that get_json returns the expected result
        """
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Create a mock response object with a json
            # method that returns test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json with the test URL
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Assert that the result is equal to test_payload
            self.assertEqual(result, test_payload)

            # Reset mock for the next iteration
            mock_get.reset_mock()
