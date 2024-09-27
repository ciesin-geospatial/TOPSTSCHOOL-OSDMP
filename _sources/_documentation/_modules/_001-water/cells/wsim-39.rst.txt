.. code:: ipython3

    from plotnine import *
    
    # plot it
    ggplot(
        cal_summaries,
        aes("month", "wsim_class_frac", fill="wsim_class", group="wsim_class")
    ) + 
    scale_fill_manual(values=leg_colors[::-1]) +
    geom_bar(stat="identity", position="stack") + 
    labs(
        title="Population Under Water Deficits in 2014 California Drought",
        subtitle="Categorized by Intensity of Deficit Return Period",
        x="",
        y="Fraction of Population*",
        caption="Population derived from Gridded Population of World (2015)",
        fill="Deficit Class") +
    theme_minimal() +
    theme(axis_text_x=element_text(rotation=25, hjust=1))
