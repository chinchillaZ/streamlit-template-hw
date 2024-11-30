import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
#logo = "https://i.imgur.com/UbOXYAU.png"
logo = " https://chinchillaz.github.io/streamlit-hw/rice_logo.png"
st.sidebar.image(logo)


st.title("農田坵塊圖")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        center=[23.1, 121.2],
         zoom=10,
        locate_control=True, 
        latlon_control=True, 
        draw_export=True, 
        minimap_control=True
    )

    m.add_basemap(basemap)
    # Add GeoJSON layer to map
    # Define the style for the GeoJSON
    geojson_style = {
        "fillColor": "#bbe299",  # Fill color
        "color": "#415430",      # Outline color
        "weight": 2,             # Outline weight
        "fillOpacity": 0.5       # Fill opacity (50%)
    }

    
    geojson_url = "https://chinchillaz.github.io/streamlit-hw/town_field.geojson"
    m.add_geojson(
        geojson_url,
        style_function=lambda feature: geojson_style
    )
    
    m.to_streamlit(height=700)
