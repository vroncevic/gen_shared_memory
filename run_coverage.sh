#!/bin/bash
#
# @brief   gen_shared_memory
# @version 2.0.0
# @date    Fri Sep 04 18:00:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_shared_memory
pylint gen_shared_memory > gen_shared_memory.report
echo "Done"
