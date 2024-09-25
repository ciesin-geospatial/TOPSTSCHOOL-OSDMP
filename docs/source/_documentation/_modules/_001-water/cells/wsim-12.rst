.. code:: ipython3

    # Plot the contiguous US boundaries for a clearer visual
    folium.GeoJson(
        contiguous_us_boundaries,
        zoom_on_click=True,
        marker=folium.Marker(icon=folium.Icon(icon="star")),
        tooltip=folium.GeoJsonTooltip(fields=["State Name"]),
        popup=folium.GeoJsonPopup(fields=["State Name"]),
        style_function=lambda x: {
            "fillColor": "orange",
            "color": "orange",
            "weight": 1,
        }
    ).add_to(us_map)
    us_map
