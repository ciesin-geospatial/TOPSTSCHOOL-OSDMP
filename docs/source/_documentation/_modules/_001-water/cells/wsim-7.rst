.. code:: ipython3

    us_boundaries = requests.get(
        "https://www.geoboundaries.org/api/current/gbOpen/USA/ADM1/"
    )
    us_boundaries = us_boundaries.json()
