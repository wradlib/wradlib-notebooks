#!/usr/bin/env bash
# Copyright (c) 2018, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

exit_status=0

testrunner -n -s
(( exit_status = ($? || $exit_status) ))

exit $exit_status
