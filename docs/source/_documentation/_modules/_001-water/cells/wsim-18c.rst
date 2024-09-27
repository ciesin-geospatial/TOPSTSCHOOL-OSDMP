.. code:: ipython3

    # check visuals
    wsim_gldas.deficit.plot(
        x="lon",
        y="lat",
        col="time",
        col_wrap=3,
        cmap="Reds_r",
        aspect=1,
        size=2,
        vmin=-60,
        vmax=0,
        cbar_kwargs={
            "orientation":"horizontal",
            "shrink":0.6,
            "label":"Deficit Anomaly"
        }
    )
