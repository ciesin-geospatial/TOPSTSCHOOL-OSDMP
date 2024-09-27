.. code:: ipython3

    wsim_gldas_texas.deficit.plot(
        col="time",
        col_wrap=3, 
        cmap="Reds_r",
        aspect=0.75,
        size=3,
        cbar_kwargs={
            "orientation": "horizontal",
            "shrink": 0.5,
            "label": "Deficit Anomaly"
        }
    )
