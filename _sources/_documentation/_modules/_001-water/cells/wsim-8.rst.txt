.. code:: ipython3

    us_boundaries = gpd.read_file(us_boundaries["gjDownloadURL"])
    us_boundaries = us_boundaries.rename(columns=lambda x: x.replace("shape", "State "))
