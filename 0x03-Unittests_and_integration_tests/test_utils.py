#!/usr/bin/env python3
"""Parametize a unit test
"""
import unittest
from unittest.mock import patch

from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test Case for Access Nested Map Function
    """

    @parameterized.expand([
        (
            {
                "a": 1
            },
            ("a", ),
            1,
        ),
        (
            {
                "a": {
                    "b": 2
                }
            },
            ("a", ),
            {
                "b": 2
            },
        ),
        (
            {
                "a": {
                    "b": 2
                }
            },
            ("a", "b"),
            2,
        ),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Unittest access_nested_map function with different inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({
            "a": 1
        }, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests access_nested_map function with different inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unittest case  for get_json function
    """

    @parameterized.expand([
        ("http://example.com", {
            "payload": True
        }),
        ("http://holberton.io", {
            "payload": False
        }),
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests get_json function
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unittest case  for test memoize
    """

    def test_memoize(self):
        """Tests memoize function
        """

        class TestClass:
            """A test class
            """

            def a_method(self):
                """method to be tested"""
                return 42

            @memoize
            def a_property(self):
                """property to be tested"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()
