.. code:: ipython3

    # group by month and class and reset the index
    cal_summaries = cal_summaries.groupby(["month", "wsim_class"])["wsim_class_pop"].sum().reset_index()
