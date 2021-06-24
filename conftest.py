#!/usr/bin/env python
# Copyright (c) 2019-2020, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

import io
import os
import sys
from distutils.version import LooseVersion

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


def pytest_collect_file(parent, path):
    if path.ext == ".ipynb":
        return NotebookFile.from_parent(parent, fspath=path)


class NotebookFile(pytest.File):

    if LooseVersion(pytest.__version__) < "5.4.0":

        @classmethod
        def from_parent(cls, parent, fspath):
            return cls(parent=parent, fspath=fspath)

    def collect(self):
        for f in [self.fspath]:
            yield NotebookItem.from_parent(self, name=os.path.basename(f))

    def setup(self):
        kernel = "python%d" % sys.version_info[0]
        self.exproc = ExecutePreprocessor(kernel_name=kernel, timeout=600)


class NotebookItem(pytest.Item):
    def __init__(self, name, parent):
        super(NotebookItem, self).__init__(name, parent)

    if LooseVersion(pytest.__version__) < "5.4.0":

        @classmethod
        def from_parent(cls, parent, name):
            return cls(parent=parent, name=name)

    def runtest(self):
        cur_dir = os.path.dirname(self.fspath)

        # See https://bugs.python.org/issue37373
        if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
            import asyncio
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        with self.fspath.open() as f:
            nb = nbformat.read(f, as_version=4)
            try:
                self.parent.exproc.preprocess(nb, {"metadata": {"path": cur_dir}})
            except CellExecutionError as e:
                raise NotebookException(e)

        with open(self.fspath, "wt", encoding='utf-8') as f:
            nbformat.write(nb, f)

    def repr_failure(self, excinfo):
        if isinstance(excinfo.value, NotebookException):
            return excinfo.exconly()

        return super(NotebookItem, self).repr_failure((excinfo))

    def reportinfo(self):
        return self.fspath, 0, "TestCase: %s" % self.name


class NotebookException(Exception):
    pass
