.. code:: ipython3

    # Load the WSIM-GLDAS dataset (12-month composite netCDF file)
    wsim_gldas = xr.open_dataset("composite_12mo.nc", engine="netcdf4")
    wsim_gldas

.. raw:: html

    <div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
    <defs>
    <symbol id="icon-database" viewBox="0 0 32 32">
    <path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
    <path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
    <path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
    </symbol>
    <symbol id="icon-file-text2" viewBox="0 0 32 32">
    <path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
    <path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
    <path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
    <path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
    </symbol>
    </defs>
    </svg>
    <style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
     *
     */
    
    :root {
      --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
      --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
      --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
      --xr-border-color: var(--jp-border-color2, #e0e0e0);
      --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
      --xr-background-color: var(--jp-layout-color0, white);
      --xr-background-color-row-even: var(--jp-layout-color1, white);
      --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
    }
    
    html[theme=dark],
    html[data-theme=dark],
    body[data-theme=dark],
    body.vscode-dark {
      --xr-font-color0: rgba(255, 255, 255, 1);
      --xr-font-color2: rgba(255, 255, 255, 0.54);
      --xr-font-color3: rgba(255, 255, 255, 0.38);
      --xr-border-color: #1F1F1F;
      --xr-disabled-color: #515151;
      --xr-background-color: #111111;
      --xr-background-color-row-even: #111111;
      --xr-background-color-row-odd: #313131;
    }
    
    .xr-wrap {
      display: block !important;
      min-width: 300px;
      max-width: 700px;
    }
    
    .xr-text-repr-fallback {
      /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
      display: none;
    }
    
    .xr-header {
      padding-top: 6px;
      padding-bottom: 6px;
      margin-bottom: 4px;
      border-bottom: solid 1px var(--xr-border-color);
    }
    
    .xr-header > div,
    .xr-header > ul {
      display: inline;
      margin-top: 0;
      margin-bottom: 0;
    }
    
    .xr-obj-type,
    .xr-array-name {
      margin-left: 2px;
      margin-right: 10px;
    }
    
    .xr-obj-type {
      color: var(--xr-font-color2);
    }
    
    .xr-sections {
      padding-left: 0 !important;
      display: grid;
      grid-template-columns: 150px auto auto 1fr 0 20px 0 20px;
    }
    
    .xr-section-item {
      display: contents;
    }
    
    .xr-section-item input {
      display: inline-block;
      opacity: 0;
    }
    
    .xr-section-item input + label {
      color: var(--xr-disabled-color);
    }
    
    .xr-section-item input:enabled + label {
      cursor: pointer;
      color: var(--xr-font-color2);
    }
    
    .xr-section-item input:focus + label {
      border: 2px solid var(--xr-font-color0);
    }
    
    .xr-section-item input:enabled + label:hover {
      color: var(--xr-font-color0);
    }
    
    .xr-section-summary {
      grid-column: 1;
      color: var(--xr-font-color2);
      font-weight: 500;
    }
    
    .xr-section-summary > span {
      display: inline-block;
      padding-left: 0.5em;
    }
    
    .xr-section-summary-in:disabled + label {
      color: var(--xr-font-color2);
    }
    
    .xr-section-summary-in + label:before {
      display: inline-block;
      content: '►';
      font-size: 11px;
      width: 15px;
      text-align: center;
    }
    
    .xr-section-summary-in:disabled + label:before {
      color: var(--xr-disabled-color);
    }
    
    .xr-section-summary-in:checked + label:before {
      content: '▼';
    }
    
    .xr-section-summary-in:checked + label > span {
      display: none;
    }
    
    .xr-section-summary,
    .xr-section-inline-details {
      padding-top: 4px;
      padding-bottom: 4px;
    }
    
    .xr-section-inline-details {
      grid-column: 2 / -1;
    }
    
    .xr-section-details {
      display: none;
      grid-column: 1 / -1;
      margin-bottom: 5px;
    }
    
    .xr-section-summary-in:checked ~ .xr-section-details {
      display: contents;
    }
    
    .xr-array-wrap {
      grid-column: 1 / -1;
      display: grid;
      grid-template-columns: 20px auto;
    }
    
    .xr-array-wrap > label {
      grid-column: 1;
      vertical-align: top;
    }
    
    .xr-preview {
      color: var(--xr-font-color3);
    }
    
    .xr-array-preview,
    .xr-array-data {
      padding: 0 5px !important;
      grid-column: 2;
    }
    
    .xr-array-data,
    .xr-array-in:checked ~ .xr-array-preview {
      display: none;
    }
    
    .xr-array-in:checked ~ .xr-array-data,
    .xr-array-preview {
      display: inline-block;
    }
    
    .xr-dim-list {
      display: inline-block !important;
      list-style: none;
      padding: 0 !important;
      margin: 0;
    }
    
    .xr-dim-list li {
      display: inline-block;
      padding: 0;
      margin: 0;
    }
    
    .xr-dim-list:before {
      content: '(';
    }
    
    .xr-dim-list:after {
      content: ')';
    }
    
    .xr-dim-list li:not(:last-child):after {
      content: ',';
      padding-right: 5px;
    }
    
    .xr-has-index {
      font-weight: bold;
    }
    
    .xr-var-list,
    .xr-var-item {
      display: contents;
    }
    
    .xr-var-item > div,
    .xr-var-item label,
    .xr-var-item > .xr-var-name span {
      background-color: var(--xr-background-color-row-even);
      margin-bottom: 0;
    }
    
    .xr-var-item > .xr-var-name:hover span {
      padding-right: 5px;
    }
    
    .xr-var-list > li:nth-child(odd) > div,
    .xr-var-list > li:nth-child(odd) > label,
    .xr-var-list > li:nth-child(odd) > .xr-var-name span {
      background-color: var(--xr-background-color-row-odd);
    }
    
    .xr-var-name {
      grid-column: 1;
    }
    
    .xr-var-dims {
      grid-column: 2;
    }
    
    .xr-var-dtype {
      grid-column: 3;
      text-align: right;
      color: var(--xr-font-color2);
    }
    
    .xr-var-preview {
      grid-column: 4;
    }
    
    .xr-index-preview {
      grid-column: 2 / 5;
      color: var(--xr-font-color2);
    }
    
    .xr-var-name,
    .xr-var-dims,
    .xr-var-dtype,
    .xr-preview,
    .xr-attrs dt {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      padding-right: 10px;
    }
    
    .xr-var-name:hover,
    .xr-var-dims:hover,
    .xr-var-dtype:hover,
    .xr-attrs dt:hover {
      overflow: visible;
      width: auto;
      z-index: 1;
    }
    
    .xr-var-attrs,
    .xr-var-data,
    .xr-index-data {
      display: none;
      background-color: var(--xr-background-color) !important;
      padding-bottom: 5px !important;
    }
    
    .xr-var-attrs-in:checked ~ .xr-var-attrs,
    .xr-var-data-in:checked ~ .xr-var-data,
    .xr-index-data-in:checked ~ .xr-index-data {
      display: block;
    }
    
    .xr-var-data > table {
      float: right;
    }
    
    .xr-var-name span,
    .xr-var-data,
    .xr-index-name div,
    .xr-index-data,
    .xr-attrs {
      padding-left: 25px !important;
    }
    
    .xr-attrs,
    .xr-var-attrs,
    .xr-var-data,
    .xr-index-data {
      grid-column: 1 / -1;
    }
    
    dl.xr-attrs {
      padding: 0;
      margin: 0;
      display: grid;
      grid-template-columns: 125px auto;
    }
    
    .xr-attrs dt,
    .xr-attrs dd {
      padding: 0;
      margin: 0;
      float: left;
      padding-right: 10px;
      width: auto;
    }
    
    .xr-attrs dt {
      font-weight: normal;
      grid-column: 1;
    }
    
    .xr-attrs dt:hover span {
      display: inline-block;
      background: var(--xr-background-color);
      padding-right: 10px;
    }
    
    .xr-attrs dd {
      grid-column: 2;
      white-space: pre-wrap;
      word-break: break-all;
    }
    
    .xr-icon-database,
    .xr-icon-file-text2,
    .xr-no-icon {
      display: inline-block;
      vertical-align: middle;
      width: 1em;
      height: 1.5em !important;
      stroke-width: 0;
      stroke: currentColor;
      fill: currentColor;
    }
    </style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt; Size: 14GB
    Dimensions:                       (lon: 1440, lat: 600, time: 793)
    Coordinates: (3)
    Data variables: (7)
    Attributes: (5)</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-6b86ea27-b93d-4d22-8954-9c78884c8eff' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-6b86ea27-b93d-4d22-8954-9c78884c8eff' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>lon</span>: 1440</li><li><span class='xr-has-index'>lat</span>: 600</li><li><span class='xr-has-index'>time</span>: 793</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-4c17987d-7def-453a-ad04-e80e99f356a5' class='xr-section-summary-in' type='checkbox'  ><label for='section-4c17987d-7def-453a-ad04-e80e99f356a5' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>lon</span></div><div class='xr-var-dims'>(lon)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-179.9 -179.6 ... 179.6 179.9</div><input id='attrs-113ab351-1e16-43ae-96a4-6011a4610876' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-113ab351-1e16-43ae-96a4-6011a4610876' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-4bb074f7-0919-4a9b-8795-a63819a9e7a7' class='xr-var-data-in' type='checkbox'><label for='data-4bb074f7-0919-4a9b-8795-a63819a9e7a7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>units :</span></dt><dd>degrees_east</dd><dt><span>long_name :</span></dt><dd>Longitude</dd><dt><span>axis :</span></dt><dd>X</dd><dt><span>standard_name :</span></dt><dd>longitude</dd></dl></div><div class='xr-var-data'><pre>array([-179.875, -179.625, -179.375, ...,  179.375,  179.625,  179.875])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>lat</span></div><div class='xr-var-dims'>(lat)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>89.88 89.62 89.38 ... -59.62 -59.88</div><input id='attrs-b3b7347f-ac60-47d8-85fa-b34961a9f898' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b3b7347f-ac60-47d8-85fa-b34961a9f898' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3de3b52b-5a9e-482d-bc8c-60567095d483' class='xr-var-data-in' type='checkbox'><label for='data-3de3b52b-5a9e-482d-bc8c-60567095d483' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>units :</span></dt><dd>degrees_north</dd><dt><span>long_name :</span></dt><dd>Latitude</dd><dt><span>axis :</span></dt><dd>Y</dd><dt><span>standard_name :</span></dt><dd>latitude</dd></dl></div><div class='xr-var-data'><pre>array([ 89.875,  89.625,  89.375, ..., -59.375, -59.625, -59.875])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1948-12-01 ... 2014-12-01</div><input id='attrs-6a42a809-d711-4f23-a7e1-a48fffc868b0' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-6a42a809-d711-4f23-a7e1-a48fffc868b0' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-fa4eba12-4698-4478-803e-26b642e916e4' class='xr-var-data-in' type='checkbox'><label for='data-fa4eba12-4698-4478-803e-26b642e916e4' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;1948-12-01T00:00:00.000000000&#x27;, &#x27;1949-01-01T00:00:00.000000000&#x27;,
           &#x27;1949-02-01T00:00:00.000000000&#x27;, ..., &#x27;2014-10-01T00:00:00.000000000&#x27;,
           &#x27;2014-11-01T00:00:00.000000000&#x27;, &#x27;2014-12-01T00:00:00.000000000&#x27;],
          dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-e3306f04-d8b9-47a8-a9cc-b83634e2bb62' class='xr-section-summary-in' type='checkbox'  ><label for='section-e3306f04-d8b9-47a8-a9cc-b83634e2bb62' class='xr-section-summary' >Data variables: <span>(7)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>deficit</span></div><div class='xr-var-dims'>(time, lat, lon)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-7d61dbbc-551a-432a-aade-50323f6b04f7' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-7d61dbbc-551a-432a-aade-50323f6b04f7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-22ad0d76-2dd7-45d1-98e6-009a95ea6008' class='xr-var-data-in' type='checkbox'><label for='data-22ad0d76-2dd7-45d1-98e6-009a95ea6008' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Composite Deficit Index</dd><dt><span>grid_mapping :</span></dt><dd>crs</dd></dl></div><div class='xr-var-data'><pre>[685152000 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>deficit_cause</span></div><div class='xr-var-dims'>(time, lat, lon)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-0a864dc1-7b03-43ce-9e71-c59c0d596ec1' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-0a864dc1-7b03-43ce-9e71-c59c0d596ec1' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-46f441d3-9b68-4b40-988f-b0990adf0641' class='xr-var-data-in' type='checkbox'><label for='data-46f441d3-9b68-4b40-988f-b0990adf0641' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Cause of Deficit</dd><dt><span>flag_values :</span></dt><dd>[1 2 3]</dd><dt><span>grid_mapping :</span></dt><dd>crs</dd><dt><span>flag_meanings :</span></dt><dd>neg_petme soil_moisture runoff_accum</dd></dl></div><div class='xr-var-data'><pre>[685152000 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>surplus</span></div><div class='xr-var-dims'>(time, lat, lon)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-8698afb6-4c0b-4174-b391-9d776f24b292' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-8698afb6-4c0b-4174-b391-9d776f24b292' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-9981fb5f-ea01-4a4d-b96a-c90dcbea23f8' class='xr-var-data-in' type='checkbox'><label for='data-9981fb5f-ea01-4a4d-b96a-c90dcbea23f8' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Composite Surplus Index</dd><dt><span>grid_mapping :</span></dt><dd>crs</dd></dl></div><div class='xr-var-data'><pre>[685152000 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>surplus_cause</span></div><div class='xr-var-dims'>(time, lat, lon)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-10bfd367-87b4-4f8b-b88a-6bcccfc1b5dc' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-10bfd367-87b4-4f8b-b88a-6bcccfc1b5dc' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-b2084b26-eec0-4f54-bbb1-1941433a2966' class='xr-var-data-in' type='checkbox'><label for='data-b2084b26-eec0-4f54-bbb1-1941433a2966' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Cause of Surplus</dd><dt><span>flag_values :</span></dt><dd>[1 2]</dd><dt><span>grid_mapping :</span></dt><dd>crs</dd><dt><span>flag_meanings :</span></dt><dd>runoff runoff_accum</dd></dl></div><div class='xr-var-data'><pre>[685152000 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>both</span></div><div class='xr-var-dims'>(time, lat, lon)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-14e8557c-0609-4623-95f1-5e0fe89889a7' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-14e8557c-0609-4623-95f1-5e0fe89889a7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-fea51eb2-d6c7-4779-8d53-8715c8579489' class='xr-var-data-in' type='checkbox'><label for='data-fea51eb2-d6c7-4779-8d53-8715c8579489' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Composite Combined Surplus &amp; Deficit Index</dd><dt><span>threshold :</span></dt><dd>3</dd><dt><span>grid_mapping :</span></dt><dd>crs</dd></dl></div><div class='xr-var-data'><pre>[685152000 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>crs</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>int32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-a0d75d8b-7888-4264-9e86-b5818c44ba3a' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-a0d75d8b-7888-4264-9e86-b5818c44ba3a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-663ccadd-3a0c-429a-83c2-f433c1397288' class='xr-var-data-in' type='checkbox'><label for='data-663ccadd-3a0c-429a-83c2-f433c1397288' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>grid_mapping_name :</span></dt><dd>latitude_longitude</dd><dt><span>longitude_of_prime_meridian :</span></dt><dd>0</dd><dt><span>semi_major_axis :</span></dt><dd>6378137</dd><dt><span>inverse_flattening :</span></dt><dd>298.257223563</dd><dt><span>spatial_ref :</span></dt><dd>GEOGCS[&quot;WGS 84&quot;,DATUM[&quot;WGS_1984&quot;,SPHEROID[&quot;WGS 84&quot;,6378137,298.257223563,AUTHORITY[&quot;EPSG&quot;,&quot;7030&quot;]],AUTHORITY[&quot;EPSG&quot;,&quot;6326&quot;]],PRIMEM[&quot;Greenwich&quot;,0,AUTHORITY[&quot;EPSG&quot;,&quot;8901&quot;]],UNIT[&quot;degree&quot;,0.0174532925199433,AUTHORITY[&quot;EPSG&quot;,&quot;9122&quot;]],AXIS[&quot;Latitude&quot;,NORTH],AXIS[&quot;Longitude&quot;,EAST],AUTHORITY[&quot;EPSG&quot;,&quot;4326&quot;]]</dd></dl></div><div class='xr-var-data'><pre>[793 values with dtype=int32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>integration_period_end_month</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>&lt;U6</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-2548e76a-8966-4fdb-94dc-209927ca8f1b' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-2548e76a-8966-4fdb-94dc-209927ca8f1b' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-6e916367-d51b-4998-937a-beac60515626' class='xr-var-data-in' type='checkbox'><label for='data-6e916367-d51b-4998-937a-beac60515626' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>units :</span></dt><dd>YYYYMM</dd></dl></div><div class='xr-var-data'><pre>[793 values with dtype=&lt;U6]</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-d2866378-87e3-456f-9f9e-c1cad4797361' class='xr-section-summary-in' type='checkbox'  ><label for='section-d2866378-87e3-456f-9f9e-c1cad4797361' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>lon</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-6ae17138-9400-4e91-9b5d-a209f1f2f956' class='xr-index-data-in' type='checkbox'/><label for='index-6ae17138-9400-4e91-9b5d-a209f1f2f956' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([-179.875, -179.625, -179.375, -179.125, -178.875, -178.625, -178.375,
           -178.125, -177.875, -177.625,
           ...
            177.625,  177.875,  178.125,  178.375,  178.625,  178.875,  179.125,
            179.375,  179.625,  179.875],
          dtype=&#x27;float64&#x27;, name=&#x27;lon&#x27;, length=1440))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>lat</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-3d8ae84a-0e2a-46a0-a05b-53e2a47be38c' class='xr-index-data-in' type='checkbox'/><label for='index-3d8ae84a-0e2a-46a0-a05b-53e2a47be38c' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([ 89.875,  89.625,  89.375,  89.125,  88.875,  88.625,  88.375,  88.125,
            87.875,  87.625,
           ...
           -57.625, -57.875, -58.125, -58.375, -58.625, -58.875, -59.125, -59.375,
           -59.625, -59.875],
          dtype=&#x27;float64&#x27;, name=&#x27;lat&#x27;, length=600))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-1c8754a8-47e5-4217-a214-c91037e1f2bf' class='xr-index-data-in' type='checkbox'/><label for='index-1c8754a8-47e5-4217-a214-c91037e1f2bf' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;1948-12-01&#x27;, &#x27;1949-01-01&#x27;, &#x27;1949-02-01&#x27;, &#x27;1949-03-01&#x27;,
                   &#x27;1949-04-01&#x27;, &#x27;1949-05-01&#x27;, &#x27;1949-06-01&#x27;, &#x27;1949-07-01&#x27;,
                   &#x27;1949-08-01&#x27;, &#x27;1949-09-01&#x27;,
                   ...
                   &#x27;2014-03-01&#x27;, &#x27;2014-04-01&#x27;, &#x27;2014-05-01&#x27;, &#x27;2014-06-01&#x27;,
                   &#x27;2014-07-01&#x27;, &#x27;2014-08-01&#x27;, &#x27;2014-09-01&#x27;, &#x27;2014-10-01&#x27;,
                   &#x27;2014-11-01&#x27;, &#x27;2014-12-01&#x27;],
                  dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, length=793, freq=None))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-a605210b-4beb-4064-82e3-7f669f362ee0' class='xr-section-summary-in' type='checkbox'  ><label for='section-a605210b-4beb-4064-82e3-7f669f362ee0' class='xr-section-summary' >Attributes: <span>(5)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>date_created :</span></dt><dd>2021-03-24T22:39:08+0000</dd><dt><span>Conventions :</span></dt><dd>CF-1.6</dd><dt><span>Title :</span></dt><dd>Water Security Indicator Model -- Global Land Data Assimilation System Data Set (WSIM-GLDAS), version 1.0: Monthly Grids</dd><dt><span>Institution :</span></dt><dd>NASA Socioeconomic Data and Applications Center (SEDAC), Center for International Earth Science Information Network (CIESIN) Columbia University</dd><dt><span>References :</span></dt><dd>Crowley, C., Baston, D., Brinks, J. 2020. Water Security Indicator Model -- Global Land Data Assimilation System Data Set (WSIM-GLDAS), version 1.0: Monthly Grids. Palisades, NY: NASA Socioeconomic Data and Applications Center.</dd></dl></div></li></ul></div></div>
