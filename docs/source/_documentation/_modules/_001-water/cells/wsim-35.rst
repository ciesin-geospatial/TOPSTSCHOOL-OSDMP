.. code:: ipython3

    # multiply
    cal_summaries["wsim_class_pop"] = (
        cal_summaries["coverage"] * cal_summaries["cell_pop_count"]
    )

    # round so we don't have fractions of people
    
    cal_summaries.wsim_class_pop = (
        cal_summaries["wsim_class_pop"]
        .astype("float")
        .round(0)
    )
    
    # check the values
    cal_summaries[:5]

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
          <th>coverage</th>
          <th>wsim_class</th>
          <th>cell_pop_count</th>
          <th>wsim_class_pop</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>January</td>
          <td>0.000052</td>
          <td>5</td>
          <td>11718.642578</td>
          <td>1.0</td>
        </tr>
        <tr>
          <th>1</th>
          <td>January</td>
          <td>0.363015</td>
          <td>6</td>
          <td>33362.726562</td>
          <td>12111.0</td>
        </tr>
        <tr>
          <th>2</th>
          <td>January</td>
          <td>0.068331</td>
          <td>7</td>
          <td>20356.484375</td>
          <td>1391.0</td>
        </tr>
        <tr>
          <th>3</th>
          <td>January</td>
          <td>0.263593</td>
          <td>6</td>
          <td>192.583374</td>
          <td>51.0</td>
        </tr>
        <tr>
          <th>4</th>
          <td>January</td>
          <td>1.0</td>
          <td>7</td>
          <td>298.508392</td>
          <td>299.0</td>
        </tr>
      </tbody>
    </table>
    </div>
