.. code:: ipython3

    # isolate only the california border
    california = contiguous_us_boundaries[
        contiguous_us_boundaries["State Name"]
        .str
        .contains("California")
    ]
    wsim_gldas_1mo = wsim_gldas_1mo.rio.write_crs("epsg: 4326")
    wsim_gldas_california = wsim_gldas_1mo.rio.clip(california.geometry.values)
    
    # give the time dimension pretty labels
    wsim_gldas_california = wsim_gldas_california.assign_coords(
        time=list(calendar.month_name[1:])
    )

    # plot it
    wsim_gldas_california.deficit.plot(
        x="lon",
        y="lat",
        col="time",
        col_wrap = 3,
        cmap = "Reds_r",
        aspect = 0.9,
        size =2.5,
        vmin = -60,
        vmax = 0,
        cbar_kwargs =  {
            "orientation": "vertical",
            "shrink": 0.6,
            "label":"Deficit Anomaly"
        }
    )
