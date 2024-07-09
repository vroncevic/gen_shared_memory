#!/bin/bash
#
# @brief   gen_shared_memory
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_shared_memory_coverage.xml gen_shared_memory_coverage.json .coverage
rm -rf fresh_new/ new_simple_test/ full_simple/ full_simple_new/ latest_pro/
ats_coverage_run.py -n gen_shared_memory -p ../README.md
rm -rf fresh_new/ new_simple_test/ full_simple/ full_simple_new/ latest_pro/
python3 -m coverage run -m --source=../gen_shared_memory unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_shared_memory_coverage.xml 
python3 -m coverage json -o gen_shared_memory_coverage.json
python3 -m coverage report --format=markdown -m
