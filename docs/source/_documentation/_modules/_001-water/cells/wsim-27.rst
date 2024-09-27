.. code:: ipython3

    # list the class breaks
    wsim_bins = [np.inf, 0, -3, -5, -10, -20, -40, -60, -np.inf]

    # classify the wsim layer with the established breaks
    wsim_class = xr.apply_ufunc(
        np.digitize,
        wsim_gldas_1mo,
        wsim_bins)
