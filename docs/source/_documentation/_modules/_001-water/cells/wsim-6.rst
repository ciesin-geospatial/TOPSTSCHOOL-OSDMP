.. code:: ipython3

    december_subset.deficit.plot(
        col="time",
        col_wrap=3, 
        cmap="Reds_r",
        aspect=2,
        size=2,
        cbar_kwargs={
            "orientation": "vertical",
            "shrink": 0.5,
            "label": "Deficit Anomaly"
        }
    )
