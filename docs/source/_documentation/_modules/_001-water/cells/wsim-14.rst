.. code:: ipython3

    # Plot Texas boundary for a clearer visual
    folium.GeoJson(
        texas_boundary,
        name="Texas",
        zoom_on_click=True,
        tooltip=folium.GeoJsonTooltip(fields=["State Name"]),
        popup=folium.GeoJsonPopup(fields=["State Name"]),
        style_function=lambda x: {
            "fillColor": "green",
            "color": "green",
            "weight": 1,
        }
    ).add_to(us_map)
    us_map
