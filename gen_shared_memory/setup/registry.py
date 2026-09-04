# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_shared_memory is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_shared_memory is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Encapsulates core gen_shared_memory components for simplification of gen_shared_memory bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_shared_memory.core.service.iservice import IService
from gen_shared_memory.core.service.isubprocessor import ISubProcessor
from gen_shared_memory.infrastructure.cli.icli import ICLI
from gen_shared_memory.setup.bundle import GenSharedMemoryBundle
from gen_shared_memory.setup.validator import GenSharedMemoryBundleValidator
from gen_shared_memory.setup.keys import GenSharedMemoryBundleKeys
from gen_shared_memory.setup.dependencies import GenSharedMemoryBundleDependencies
from gen_shared_memory.setup.dep_validator import GenSharedMemoryBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_shared_memory'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_shared_memory/blob/dev/LICENSE'
__version__ = '2.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSharedMemoryBundleRegistry:
    '''
        Encapsulates core gen_shared_memory components for simplification of gen_shared_memory bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_shared_memory bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenSharedMemoryBundleDependencies) -> GenSharedMemoryBundle:
        '''
            Creates the gen_shared_memory bundle.

            :param dependencies: The gen_shared_memory bundle dependencies.
            :return: The gen_shared_memory bundle.
            :exceptions:
                | ATSValueError: The gen_shared_memory bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_shared_memory bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_shared_memory bundle must be provided and have proper values.
                | ATSTypeError:  The gen_shared_memory bundle must be an instance of GenSharedMemoryBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenSharedMemoryBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenSharedMemoryBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenSharedMemoryBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenSharedMemoryBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenSharedMemoryBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenSharedMemoryBundle = GenSharedMemoryBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenSharedMemoryBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
