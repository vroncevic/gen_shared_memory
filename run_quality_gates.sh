#!/bin/bash
#
# @brief   gen_shared_memory
# @version 2.0.0
# @date    Fri Sep 04 18:00:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_shared_memory
python3 gates/gates/isp_checker.py gen_shared_memory
python3 gates/gates/limits_checker.py gen_shared_memory
python3 gates/gates/srp_checker.py gen_shared_memory

echo "Done"
