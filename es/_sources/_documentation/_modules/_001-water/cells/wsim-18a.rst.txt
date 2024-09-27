.. code:: ipython3


    wsim_gldas = xr.open_dataset("composite_12mo.nc, engine = "h5netcdf")

    # list of dates we want to keep
    keeps = pd.date_range(start="2000-12-01", end="2014-12-01", freq = "YS-DEC")

    # subset for the dates
    wsim_gldas = wsim_gldas.sel(time=keeps)

    # subset for the variable of interest and the crs info
    wsim_gldas = wsim_gldas[["deficit", "crs"]]

    # give the time variable pretty names
    wsim_gldas = wsim_gldas.assign_coords(time=list(range(2000, 2015)))

    # clip wsim_gldas
    wsim_gldas = wsim_gldas.rio.write_crs("epsg: 4326")
    wsim_gldas = wsim_gldas.rio.clip(usa.geometry.values)
