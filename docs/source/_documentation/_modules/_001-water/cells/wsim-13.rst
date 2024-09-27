.. code:: ipython3

    # Extract and visualize the boundary for a specific state (e.g., Texas)
    texas_boundary = contiguous_us_boundaries[contiguous_us_boundaries["State Name"].str.contains("Texas")]
