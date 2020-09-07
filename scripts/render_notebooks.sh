#!/usr/bin/env bash
# Copyright (c) 2018-2020, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

exit_status=0

pytest -n 2 --verbose --durations=15 notebooks
(( exit_status = ($? || $exit_status) ))

exit $exit_status
