#!/bin/bash
# Copyright (c) 2017, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

exit_status=0

$HOME/wradlib/testrunner.py -n -s
 (( exit_status = ($? || $exit_status) ))

exit $exit_status
