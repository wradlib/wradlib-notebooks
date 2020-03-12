#!/usr/bin/env python
# Copyright (c) 2019-2020, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

import pytest
import sys
import io
import os

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


def pytest_collect_file(path, parent):
    if path.ext == ".ipynb":
        return NotebookFile(path, parent)


class NotebookFile(pytest.File):
    def collect(self):
        for f in [self.fspath]:
            yield NotebookItem(os.path.basename(f), self)

    def setup(self):
        kernel = 'python%d' % sys.version_info[0]
        self.exproc = ExecutePreprocessor(kernel_name=kernel, timeout=600)


class NotebookItem(pytest.Item):
    def __init__(self, name, parent):
        super(NotebookItem, self).__init__(name, parent)

    def runtest(self):
        cur_dir = os.path.dirname(self.fspath)

        with self.fspath.open() as f:
            nb = nbformat.read(f, as_version=4)
            try:
                self.parent.exproc.preprocess(nb,
                                              {'metadata': {'path': cur_dir}})
            except CellExecutionError as e:
                raise NotebookException(e)

        with io.open(self.fspath, 'wt') as f:
            nbformat.write(nb, f)

    def repr_failure(self, excinfo):
        if isinstance(excinfo.value, NotebookException):
            return f"{excinfo.value}\n{excinfo.traceback}"

    def reportinfo(self):
        return self.fspath, 0, "TestCase: %s" % self.name


class NotebookException(Exception):
    pass
