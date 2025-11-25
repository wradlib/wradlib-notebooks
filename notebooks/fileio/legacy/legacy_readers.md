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

```{include} ../../../_includes/license_block.md
```
# Legacy readers

```{warning}
For radar data in polar format the [openradar community](https://openradarscience.org/) published [xradar](https://docs.openradarscience.org/projects/xradar/en/latest/) where xarray-based readers/writers are implemented. That particular code was ported from $\omega radlib$ to xradar. Please refer to xradar for enhancements for polar radar.

From $\omega radlib$ version 1.19 that functionality is imported from [xradar](https://github.com/openradar/xradar)-package whenever and wherever necessary.

Please refer to [xradar based examples](../backends/xarray_backends) for an introduction.
```

Since new developments are done in xradar this chapter only covers the legacy readers with numpy output. They will work fine, but we recommend to use the available xarray based readers.

Reading weather radar files is done via the {mod}`wradlib.io` module. There you will find a complete function reference.

```{toctree}
:hidden:
:maxdepth: 2
DWD DX <read_dx>
NetCDF <read_netcdf>
HDF5 <read_hdf5>
OPERA ODIM <read_odim>
GAMIC HDF <read_gamic>
Leonardo Rainbow <read_rainbow>
Vaisala IRIS/Sigmet <read_iris>
```