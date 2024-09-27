.. code:: ipython3

    # sum the population by month
    cal_summaries["month_pop"] = (
        cal_summaries
        .groupby(["month"])["wsim_class_pop"]
        .transform("sum")
    )

    # divide the class total by month sum to get the fraction
    cal_summaries["wsim_class_frac"] = (
        cal_summaries["wsim_class_pop"] / cal_summaries["month_pop"]
    )
    
    # check the values
    cal_summaries

.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>month</th>
          <th>wsim_class</th>
          <th>wsim_class_pop</th>
          <th>month_pop</th>
          <th>wsim_class_frac</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>April</td>
          <td>0</td>
          <td>407597.0</td>
          <td>36565982.0</td>
          <td>0.011147</td>
        </tr>
        <tr>
          <th>1</th>
          <td>April</td>
          <td>3</td>
          <td>115254.0</td>
          <td>36565982.0</td>
          <td>0.003152</td>
        </tr>
        <tr>
          <th>2</th>
          <td>April</td>
          <td>4</td>
          <td>5217618.0</td>
          <td>36565982.0</td>
          <td>0.142690</td>
        </tr>
        <tr>
          <th>3</th>
          <td>April</td>
          <td>5</td>
          <td>20640931.0</td>
          <td>36565982.0</td>
          <td>0.564485</td>
        </tr>
        <tr>
          <th>4</th>
          <td>April</td>
          <td>6</td>
          <td>6052406.0</td>
          <td>36565982.0</td>
          <td>0.165520</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>76</th>
          <td>September</td>
          <td>3</td>
          <td>6428278.0</td>
          <td>36565982.0</td>
          <td>0.175799</td>
        </tr>
        <tr>
          <th>77</th>
          <td>September</td>
          <td>4</td>
          <td>6369109.0</td>
          <td>36565982.0</td>
          <td>0.174181</td>
        </tr>
        <tr>
          <th>78</th>
          <td>September</td>
          <td>5</td>
          <td>4146780.0</td>
          <td>36565982.0</td>
          <td>0.113405</td>
        </tr>
        <tr>
          <th>79</th>
          <td>September</td>
          <td>6</td>
          <td>4651595.0</td>
          <td>36565982.0</td>
          <td>0.127211</td>
        </tr>
        <tr>
          <th>80</th>
          <td>September</td>
          <td>7</td>
          <td>13125040.0</td>
          <td>36565982.0</td>
          <td>0.358941</td>
        </tr>
      </tbody>
    </table>
    <p>81 rows × 5 columns</p>
    </div>
