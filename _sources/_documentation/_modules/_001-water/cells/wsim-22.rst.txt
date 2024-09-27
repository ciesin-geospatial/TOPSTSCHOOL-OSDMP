.. code:: ipython3

    usa_counties = requests.get(
        "https://www.geoboundaries.org/api/current/gbOpen/USA/ADM2/"
    )
    
    # parse the request for the data
    usa_counties = usa_counties.json()
    usa_counties = gpd.read_file(usa_counties["gjDownloadURL"])

    # intersect california state level with usa counties

    california_counties = usa_counties.overlay(california, how="intersection")
    california_counties.plot()
