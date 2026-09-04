# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_shared_memory bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_shared_memory.setup.bundle import GenSharedMemoryBundle
from gen_shared_memory.setup.options import GenSharedMemoryBundleOptions
from gen_shared_memory.setup.registry import GenSharedMemoryBundleRegistry
from gen_shared_memory.setup.dependencies import GenSharedMemoryBundleDependencies
from gen_shared_memory.setup.opt_validator import GenSharedMemoryBundleOptionsValidator
from gen_shared_memory.setup.keys import GenSharedMemoryBundleKeys
from gen_shared_memory.core.service.engine import Service
from gen_shared_memory.infrastructure.subprocessor import SubProcessor
from gen_shared_memory.infrastructure.cli.engine import CLI
from gen_shared_memory.infrastructure.cli.setup.bundle import CLIBundle
from gen_shared_memory.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_shared_memory.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_shared_memory.infrastructure.command.command import CommandBundle
from gen_shared_memory.infrastructure.command.gen_shared_memory_command_definition import GenSharedMemoryCommandDefinition
from gen_shared_memory.infrastructure.command.gen_shared_memory_command_executor import GenSharedMemoryCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_shared_memory'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_shared_memory/blob/dev/LICENSE'
__version__ = '2.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSharedMemoryBundleFactory:
    '''
        Factory for creating the gen_shared_memory bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_shared_memory info file.
            :methods:
                | create_bundle - Creates the gen_shared_memory bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = 'gen_shared_memory/infrastructure/config/gen_shared_memory.cfg'

    @classmethod
    def create_bundle(cls, options: GenSharedMemoryBundleOptions | None = None) -> GenSharedMemoryBundle:
        '''
            Creates the gen_shared_memory bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_shared_memory bundle.
            :return: The gen_shared_memory bundle.
            :exceptions:
                | ATSValueError: The gen_shared_memory bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_shared_memory bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_shared_memory bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_shared_memory bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_shared_memory bundle must be provided and have proper values.
                | ATSTypeError:  The gen_shared_memory bundle must be an instance of GenSharedMemoryBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenSharedMemoryBundleOptionsValidator.validate(options)

        info_file = options.get(GenSharedMemoryBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_shared_memory_definition: GenSharedMemoryCommandDefinition = GenSharedMemoryCommandDefinition()

        gen_shared_memory_bundle: CommandBundle = CommandBundle(
            definition=gen_shared_memory_definition,
            executor=GenSharedMemoryCommandExecutor(gen_shared_memory_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_shared_memory_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenSharedMemoryBundleRegistry.create_bundle(
            dependencies=GenSharedMemoryBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
