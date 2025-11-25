---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: python3
  display_name: Python 3
---

```{include} ../../_includes/license_block.md
```
# Computing cartesian and geographical coordinates for polar data

```{code-cell} python
import warnings

import numpy as np
import wradlib as wrl
import wradlib_data
import xradar as xd

warnings.filterwarnings("ignore")
```

## Read the data

Here, we use an OPERA hdf5 dataset.

```{code-cell} python
filename = "hdf5/20130429043000.rad.bewid.pvol.dbzh.scan1.hdf"
filename = wradlib_data.DATASETS.fetch(filename)
pvol = xd.io.open_odim_datatree(filename)
display(pvol)
```

## Retrieve azimuthal equidistant coordinates and projection

```{code-cell} python
for key in list(pvol.children):
    if "sweep" in key:
        pvol[key].ds = pvol[key].ds.wrl.georef.georeference()
```

```{code-cell} python
pvol["sweep_0"].ds.DBZH.plot(x="x", y="y")
```

## Retrieve geographic coordinates (longitude and latitude)


### Using crs-keyword argument.

```{code-cell} python
for key in list(pvol.children):
    if "sweep" in key:
        pvol[key].ds = pvol[key].ds.wrl.georef.georeference(
            crs=wrl.georef.get_default_projection()
        )
```

```{code-cell} python
ds1 = pvol["sweep_0"].ds.wrl.georef.georeference(
    crs=wrl.georef.get_default_projection()
)
ds1.DBZH.plot(x="x", y="y")
```

### Using reproject

```{code-cell} python
ds2 = pvol["sweep_0"].ds.wrl.georef.reproject(
    trg_crs=wrl.georef.epsg_to_osr(32632),
)
ds2.DBZH.plot(x="x", y="y")
```
