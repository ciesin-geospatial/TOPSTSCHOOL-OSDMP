.. code:: ipython3

    # check first 10 rows
    cc_summaries[0:10]

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
          <th>county</th>
          <th>January</th>
          <th>February</th>
          <th>March</th>
          <th>April</th>
          <th>May</th>
          <th>June</th>
          <th>July</th>
          <th>August</th>
          <th>September</th>
          <th>October</th>
          <th>November</th>
          <th>December</th>
          <th>geometry</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Alpine</td>
          <td>-41.762840</td>
          <td>-16.325728</td>
          <td>-13.645101</td>
          <td>-8.343272</td>
          <td>-28.199846</td>
          <td>-29.179775</td>
          <td>-25.325485</td>
          <td>-14.808689</td>
          <td>-14.582643</td>
          <td>-4.376792</td>
          <td>-4.113872</td>
          <td>-5.714340</td>
          <td>POLYGON ((-119.57953 38.70561, -119.59866 38.6...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Mohave</td>
          <td>-41.926029</td>
          <td>-7.661513</td>
          <td>-9.152430</td>
          <td>-14.206533</td>
          <td>-60.000000</td>
          <td>-10.475436</td>
          <td>-6.967257</td>
          <td>-7.795761</td>
          <td>-2.742674</td>
          <td>-4.661378</td>
          <td>-6.620070</td>
          <td>-11.090995</td>
          <td>MULTIPOLYGON (((-114.48678 34.71911, -114.4860...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Tuolumne</td>
          <td>-46.240213</td>
          <td>-19.108027</td>
          <td>-16.389606</td>
          <td>-8.347591</td>
          <td>-42.286756</td>
          <td>-24.053486</td>
          <td>-22.873270</td>
          <td>-26.276834</td>
          <td>-29.332736</td>
          <td>-5.976634</td>
          <td>-3.198179</td>
          <td>-2.996842</td>
          <td>POLYGON ((-119.88476 38.35619, -119.86968 38.3...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Tehama</td>
          <td>-57.917277</td>
          <td>-49.567668</td>
          <td>-23.608668</td>
          <td>-21.017951</td>
          <td>-28.339994</td>
          <td>-46.608842</td>
          <td>-42.693579</td>
          <td>-33.756402</td>
          <td>-8.716129</td>
          <td>-1.808360</td>
          <td>-7.166282</td>
          <td>-5.475178</td>
          <td>POLYGON ((-121.49789 40.43201, -121.47404 40.4...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Trinity</td>
          <td>-59.978625</td>
          <td>-45.856119</td>
          <td>-45.540983</td>
          <td>-25.803624</td>
          <td>-43.663656</td>
          <td>-60.000000</td>
          <td>-60.000000</td>
          <td>-46.338076</td>
          <td>-2.438062</td>
          <td>2.108574</td>
          <td>-6.474706</td>
          <td>-7.222751</td>
          <td>POLYGON ((-123.05144 40.26815, -123.01859 40.2...</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Curry</td>
          <td>-60.000000</td>
          <td>-56.224870</td>
          <td>-26.244996</td>
          <td>-4.247256</td>
          <td>-9.093711</td>
          <td>-54.969276</td>
          <td>-60.000000</td>
          <td>-60.000000</td>
          <td>-2.081964</td>
          <td>2.505597</td>
          <td>-5.030906</td>
          <td>-5.104263</td>
          <td>MULTIPOLYGON (((-124.12621 41.997, -124.21162 ...</td>
        </tr>
        <tr>
          <th>6</th>
          <td>San Benito</td>
          <td>-60.000000</td>
          <td>-60.000000</td>
          <td>-55.619817</td>
          <td>-23.027860</td>
          <td>-60.000000</td>
          <td>-60.000000</td>
          <td>-60.000000</td>
          <td>-59.993260</td>
          <td>-60.000000</td>
          <td>-59.984706</td>
          <td>-37.763730</td>
          <td>-4.135725</td>
          <td>POLYGON ((-121.62947 36.91169, -121.60737 36.8...</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Josephine</td>
          <td>-60.000000</td>
          <td>-22.464207</td>
          <td>-25.885935</td>
          <td>-14.265512</td>
          <td>-13.829797</td>
          <td>-32.273193</td>
          <td>-60.000000</td>
          <td>-43.312246</td>
          <td>-12.886647</td>
          <td>1.938376</td>
          <td>-6.264188</td>
          <td>-8.443334</td>
          <td>MULTIPOLYGON (((-123.81401 41.9951, -123.82149...</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Sierra</td>
          <td>-19.329339</td>
          <td>-18.765692</td>
          <td>-11.403096</td>
          <td>-11.497562</td>
          <td>-18.052833</td>
          <td>-27.915046</td>
          <td>-27.949060</td>
          <td>-14.572026</td>
          <td>-6.030163</td>
          <td>-5.473642</td>
          <td>-1.692186</td>
          <td>-30.551402</td>
          <td>POLYGON ((-120.00937 39.44512, -120.03522 39.4...</td>
        </tr>
        <tr>
          <th>9</th>
          <td>El Dorado</td>
          <td>-44.008753</td>
          <td>-17.298188</td>
          <td>-12.065714</td>
          <td>-9.303977</td>
          <td>-33.611919</td>
          <td>-28.847394</td>
          <td>-25.674937</td>
          <td>-12.958253</td>
          <td>-5.670928</td>
          <td>-6.029936</td>
          <td>-2.770664</td>
          <td>-10.949467</td>
          <td>POLYGON ((-119.90433 38.93333, -119.88766 38.9...</td>
        </tr>
      </tbody>
    </table>
    </div>
