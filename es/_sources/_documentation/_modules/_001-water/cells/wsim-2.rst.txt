.. code:: ipython3

    xr.set_options(
        keep_attrs=True,
        display_expand_attrs=False,
        display_expand_coords=False,
        display_expand_data=False,
        display_expand_data_vars=False
    )
    %config InlineBackend.figure_format="retina"
    small: int = 6
    medium: int = 10
    large: int = 14
    params = {
        "axes.labelsize": medium,
        "axes.spines.right": False
        "axes.spines.top": False
        "axes.titlesize": medium,
        "axes.titlesize": medium,
        "figure.figsize": (16, 10),
        "figure.titlesize": large,
        "image.interpolation": "nearest",
        "image.origin": "lower",
        "legend.fontsize": medium,
        "xtick.labelsize": medium,
        "ytick.labelsize": medium,
    }
    plt.rcParams.update(params)
    plt.style.use("seaborn-v0_8-whitegrid")
