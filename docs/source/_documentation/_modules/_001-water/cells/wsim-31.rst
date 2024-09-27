.. code:: ipython3

    # select just columns with word "coverage" in them
    cal_wsim_cov = cal_wsim_gpw.filter(like="coverage", axis=1)

    # rename them for months
    cal_wsim_cov.columns = calendar.month_name[1:]
    
    # melt them and create new columns; month and coverage
    cal_wsim_cov= pd.melt(
        cal_wsim_cov, var_name="month", value_name="coverage"
    )
