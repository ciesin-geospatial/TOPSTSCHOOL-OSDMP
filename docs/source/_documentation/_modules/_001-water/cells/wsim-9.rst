.. code:: ipython3

    us_map = folium.Map([43, -100], tiles="cartodbpositron", zoom_start=5)
    folium.GeoJson(
        us_boundaries,
        name="USA",
        zoom_on_click=True,
        marker=folium.Marker(icon=folium.Icon(icon="star")),
        tooltip=folium.GeoJsonTooltip(fields=["State Name"]),
        popup=folium.GeoJsonPopup(fields=["State Name"]),
        style_function=lambda x: {
            "fillColor": "red",
            "color": "red",
            "weight": 1,
        }
    ).add_to(us_map)
    us_map
