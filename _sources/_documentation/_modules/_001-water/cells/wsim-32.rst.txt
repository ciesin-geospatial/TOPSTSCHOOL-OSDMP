.. code:: ipython3

    # select just columns with word "coverage" in them
    cal_wsim_val = cal_wsim_gpw.filter(like="values", axis=1)
    
    # rename them for months
    cal_wsim_val.columns = calendar.month_name[1:]
    
    # melt them and create new columns; month and wsim class
    cal_wsim_val= pd.melt(
        cal_wsim_val, var_name="month", value_name="wsim_class"
    )
