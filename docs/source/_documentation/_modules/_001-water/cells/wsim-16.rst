.. code:: ipython3

    wsim_gldas_texas = december_subset.rio.clip(texas_boundary.geometry.values)
