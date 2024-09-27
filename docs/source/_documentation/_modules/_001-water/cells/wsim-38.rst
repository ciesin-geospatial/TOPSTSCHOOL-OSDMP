.. code:: ipython3

    # wsim class as category
    cal_summaries["wsim_class"] = (
        cal_summaries["wsim_class"].astype("category")
    )
    
    # give ordinal pretty labels
    cal_summaries["wsim_class"] = (
        cal_summaries["wsim_class"]
        .cat
        .rename_categories(
            {0: "0",
            1: "-3",
            2: "-5",
            3: "-10",
            4: "-20",
            5: "-40",
            6: "-50",
            7: "-60"}
        )
    )
    
    # same for the months
    cal_summaries["month"] = pd.Categorical(
        cal_summaries["month"],
        categories=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ],
        ordered=True
    )
    
    # set our desired palette
    leg_colors=[
        "#9B0039",  # -50 to -40
        "#D44135",  # -40 to -20
        "#FF8D43",  # -20 to -10
        "#FFC754",  # -10 to -5
        "#FFEDA3",  # -5 to -3
        "#fffdc7",  # -3 to 0
        "#FFF4C7",  # 0-3
        "#FFFFFF"
    ]
