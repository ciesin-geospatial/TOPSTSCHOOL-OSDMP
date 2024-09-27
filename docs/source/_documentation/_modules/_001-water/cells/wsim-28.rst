.. code:: ipython3

    # run the extraction
    cal_wsim_gpw = exact_extract(
        wsim_class.deficit, 
        california_counties, 
        ["coverage", "values", "weights"], 
        output="pandas", 
        include_geom=False, 
        weights=gpw
    )
