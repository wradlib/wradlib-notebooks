---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3
---

```{include} ../../_includes/license_block.md
```
# Import wradlib and check its version

This simple example shows the $\omega radlib$ version at rendering time.

```{code-cell} python
import wradlib

print(wradlib.__version__)
```
