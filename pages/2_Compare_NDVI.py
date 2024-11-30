import streamlit as st
import leafmap.foliumap as leafmap
import folium

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = " https://chinchillaz.github.io/streamlit-hw/rice_logo.png"
st.sidebar.image(logo)

st.title("颱風前乾淨影像 比較NDVI")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            #left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
            left_layer="https://chinchillaz.github.io/streamlit-hw/ndvi_20240901_field.tif", 
            right_layer="https://chinchillaz.github.io/streamlit-hw/ndvi_20240911_field.tif",
            left_colormap="RdYlGn",  # Apply the 'RdYlGn' colormap for the left layer
            right_colormap="RdYlGn"  # Apply the 'RdYlGn' colormap for the right layer
        )
        #m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

         # Add text markers for the dates
        folium.Marker(
            location=[23.1, 121.2],  # Approximate location for the marker
            popup="Date: 20240901",  # Popup text
            icon=folium.Icon(color="green")
        ).add_to(m)

        folium.Marker(
            location=[23.1, 121.4],  # Slightly different location for the second marker
            popup="Date: 20240911",  # Popup text
            icon=folium.Icon(color="blue")
        ).add_to(m)


m.to_streamlit(height=700)
