.. code:: ipython3

    # concactenate them back together
    cal_summaries = pd.concat(
        [cal_wsim_cov,                      # just the coverages values
        cal_wsim_val["wsim_class"],         # just the class values
        cal_wsim_weight["cell_pop_count"]], # just the pop count values
        axis=1
    )
    
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
          <th>coverage</th>
          <th>wsim_class</th>
          <th>cell_pop_count</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>January</td>
          <td>0.000052</td>
          <td>5</td>
          <td>11718.642578</td>
        </tr>
        <tr>
          <th>1</th>
          <td>January</td>
          <td>0.363015</td>
          <td>6</td>
          <td>33362.726562</td>
        </tr>
        <tr>
          <th>2</th>
          <td>January</td>
          <td>0.068331</td>
          <td>7</td>
          <td>20356.484375</td>
        </tr>
        <tr>
          <th>3</th>
          <td>January</td>
          <td>0.263593</td>
          <td>6</td>
          <td>192.583374</td>
        </tr>
        <tr>
          <th>4</th>
          <td>January</td>
          <td>1.0</td>
          <td>7</td>
          <td>298.508392</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>15907</th>
          <td>December</td>
          <td>0.08602</td>
          <td>2</td>
          <td>788672.6875</td>
        </tr>
        <tr>
          <th>15908</th>
          <td>December</td>
          <td>0.00022</td>
          <td>5</td>
          <td>2462.314941</td>
        </tr>
        <tr>
          <th>15909</th>
          <td>December</td>
          <td>0.001785</td>
          <td>5</td>
          <td>8885.547852</td>
        </tr>
        <tr>
          <th>15910</th>
          <td>December</td>
          <td>0.00063</td>
          <td>4</td>
          <td>25215.951172</td>
        </tr>
        <tr>
          <th>15911</th>
          <td>December</td>
          <td>0.000264</td>
          <td>4</td>
          <td>396.317535</td>
        </tr>
      </tbody>
    </table>
    <p>15912 rows × 4 columns</p>
    </div>
