.. code:: ipython3

    # Keep only the continental USA boundaries
    contiguous_us_boundaries = us_boundaries[~us_boundaries["State Name"].isin(excluded_areas)]
