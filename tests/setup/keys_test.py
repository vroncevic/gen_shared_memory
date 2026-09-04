# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenSharedMemoryBundleKeys class.
'''

from __future__ import annotations

from unittest import TestCase
from types import MappingProxyType

from gen_shared_memory.setup.keys import GenSharedMemoryBundleKeys


class TestGenSharedMemoryBundleKeys(TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenSharedMemoryBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenSharedMemoryBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenSharedMemoryBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenSharedMemoryBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenSharedMemoryBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenSharedMemoryBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenSharedMemoryBundleKeys.OPTION_INFO_FILE, opts)
