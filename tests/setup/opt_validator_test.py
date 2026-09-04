# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenSharedMemoryBundleOptionsValidator class.
'''

from __future__ import annotations

from unittest import TestCase

from gen_shared_memory.setup.opt_validator import GenSharedMemoryBundleOptionsValidator


class TestGenSharedMemoryBundleOptionsValidator(TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenSharedMemoryBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenSharedMemoryBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenSharedMemoryBundleOptionsValidator.validate("not_a_mapping")

        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenSharedMemoryBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenSharedMemoryBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenSharedMemoryBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenSharedMemoryBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenSharedMemoryBundleOptionsValidator.is_valid({'info_file': 123}))
