.. code:: ipython3

    import matplotlib.pyplot as plt

    # setup the panels for the figures
    fig, axs = plt.subplots(
        4, 3, figsize=(8, 8), facecolor="w", sharex=True, sharey=True
    )

    # convert list of 2D axis positions into a 1d list of number 1-12
    axs = axs.ravel()
    fig.tight_layout()
    fig.suptitle("Monthly California Deficits for 2014", fontsize=14, y=1.05)

    # loop through columns to make the plot for each month
    for i, month in enumerate(cc_summaries.columns[1:13]):
        axs[i].set_title(month, fontsize= 11)
        cc_summaries.plot(column=month, ax=axs[i], cmap = "Reds_r")
        california_counties.plot(
            ax=axs[i], edgecolor="black", color="none", linewidth=0.25
        )
    
    # loop through again and turn off the axes for a cleaner map
    for ax in axs:
        ax.axis("off")

    patch_col = axs[0].collections[0]
    cb = fig.colorbar(patch_col, ax=axs, shrink=0.5, label = "Deficit Anomaly")
