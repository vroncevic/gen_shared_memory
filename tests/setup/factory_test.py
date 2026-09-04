# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenSharedMemoryBundleFactory class.
'''

from __future__ import annotations

from unittest import TestCase

from gen_shared_memory.setup.bundle import GenSharedMemoryBundle
from gen_shared_memory.setup.factory import GenSharedMemoryBundleFactory


class TestGenSharedMemoryBundleFactory(TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenSharedMemoryBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenSharedMemoryBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_shared_memory/infrastructure/config/gen_shared_memory.cfg'}
        bundle = GenSharedMemoryBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenSharedMemoryBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenSharedMemoryBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenSharedMemoryBundleFactory.get_version(), '2.0.0')
