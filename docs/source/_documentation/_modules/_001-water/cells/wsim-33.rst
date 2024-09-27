.. code:: ipython3

    # select just columns with word "coverage" in them
    cal_wsim_weight = cal_wsim_gpw.filter(like="weight", axis=1)

    # rename them for months
    cal_wsim_weight.columns = calendar.month_name[1:]
    
    # melt them and create new columns; month and population count
    cal_wsim_weight= pd.melt(
        cal_wsim_weight, var_name="month", value_name="cell_pop_count"
    )
