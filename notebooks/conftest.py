#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2025, wradlib developers.
# Distributed under the MIT License. See LICENSE-MIT for more info.


from pathlib import Path

import jupytext
import nbformat
import pytest
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


def pytest_configure(config):
    config.addinivalue_line("norecursedirs", "_build")


def pytest_collect_file(parent, file_path: Path):
    if file_path.suffix in (".md",):
        return NotebookFile.from_parent(parent=parent, path=file_path)


class NotebookFile(pytest.File):
    @classmethod
    def from_parent(cls, parent, path):
        return super().from_parent(parent=parent, path=path)

    def collect(self):
        yield NotebookItem.from_parent(parent=self, name=self.path.name)


class NotebookItem(pytest.Item):
    def __init__(self, name, parent):
        super().__init__(name, parent)

    def runtest(self):
        # Load notebook (MyST .md or .ipynb)
        if self.parent.path.suffix == ".md":
            nb = jupytext.read(self.parent.path)

        # ensure NotebookNode
        if not isinstance(nb, nbformat.NotebookNode):
            nb = nbformat.from_dict(nb)

        # ensure kernel info
        nb.metadata.setdefault(
            "kernelspec",
            {"name": "python3", "display_name": "Python 3", "language": "python"},
        )

        # clear previous outputs, if any
        for cell in nb.cells:
            if cell.cell_type == "code":
                cell.outputs = []
                cell.execution_count = None

        # execute notebook
        client = NotebookClient(
            nb,
            kernel_name="python3",
            timeout=600,
            iopub_timeout=600,
            allow_errors=False,
        )
        try:
            client.execute()
        except CellExecutionError as e:
            raise NotebookException(e) from e

    def repr_failure(self, excinfo):
        if isinstance(excinfo.value, NotebookException):
            return excinfo.exconly()
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.parent.path, 0, f"TestCase: {self.name}"


class NotebookException(Exception):
    pass
