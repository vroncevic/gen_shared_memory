# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
Info
    Unit tests for GenSharedMemoryBundleRegistry class.
'''

from __future__ import annotations

from unittest import TestCase
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_shared_memory.core.service.iservice import IService
from gen_shared_memory.core.service.isubprocessor import ISubProcessor
from gen_shared_memory.infrastructure.cli.icli import ICLI
from gen_shared_memory.setup.bundle import GenSharedMemoryBundle
from gen_shared_memory.setup.registry import GenSharedMemoryBundleRegistry


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenSharedMemoryBundleRegistry(TestCase):

    def test_create_bundle_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }

        bundle = GenSharedMemoryBundleRegistry.create_bundle(dependencies)
        self.assertIsInstance(bundle, GenSharedMemoryBundle)
        self.assertEqual(bundle.base, mock_base)

    def test_create_bundle_invalid_dependencies(self) -> None:
        with self.assertRaises(Exception):
            GenSharedMemoryBundleRegistry.create_bundle(None)

    def test_get_version(self) -> None:
        self.assertEqual(GenSharedMemoryBundleRegistry.get_version(), '2.0.0')
