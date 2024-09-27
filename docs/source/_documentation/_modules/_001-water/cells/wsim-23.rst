.. code:: ipython3

    from exactextract import exact_extract

    # run the extraction
    cc_summaries = exact_extract(
        wsim_gldas_california.deficit,
        california_counties,
        "mean",
        output="pandas",
        include_cols="shapeName",
        include_geom=True
    )

    # make the column names pretty
    col_names = [["county"], calendar.month_name[1:], ["geometry"]]
    col_names = sum(col_names, [])
    cc_summaries.columns = col_names
