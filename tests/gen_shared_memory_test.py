# -*- coding: UTF-8 -*-

'''
Module
    gen_shared_memory_test.py
Copyright
    Copyright (C) 2018 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_shared_memory is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_shared_memory is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class GenSharedMemoryTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenSharedMemory.
Execute
    python3 -m unittest -v gen_shared_memory_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from gen_shared_memory import GenSharedMemory
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_shared_memory'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_shared_memory/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSharedMemoryTestCase(TestCase):
    '''
        Defines class GenSharedMemoryTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenSharedMemory.
        GenSharedMemory unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_arg - Test wrong arg.
                | test_process - Generate project structure.
                | test_tool_not_operational - Test not operational.
                | test_pro_already_exists - Test pro already exists.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: GenSharedMemory = GenSharedMemory()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: GenSharedMemory = GenSharedMemory()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Test wrong arg'''
        sys.argv.clear()
        sys.argv.insert(0, '-d')
        sys.argv.insert(1, 'wrong_pro')
        generator: GenSharedMemory = GenSharedMemory()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'latest_pro')
        generator: GenSharedMemory = GenSharedMemory()
        self.assertTrue(generator.process())

    def test_tool_not_operational(self) -> None:
        '''Test not operational'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'fresh')
        generator: GenSharedMemory = GenSharedMemory()
        generator.tool_operational = False
        self.assertFalse(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Test pro already exists'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'fresh_new')
        generator: GenSharedMemory = GenSharedMemory()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
