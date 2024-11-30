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

        # Add the custom legend to the left side of the map
        legend_html = """
        <div style="position: fixed; 
                    top: 10px; left: 10px; width: 200px; height: 150px; 
                    border:2px solid grey; background-color:white; 
                    z-index:9999; font-size:14px; padding: 10px;">
        <b>NDVI Color Legend</b><br>
        <img src="https://www.colorhexa.com/ff0000.png" width="30" height="30"> Low NDVI (Red)<br>
        <img src="https://www.colorhexa.com/00ff00.png" width="30" height="30"> High NDVI (Green)<br>
        </div>
        """
        m.get_root().html.add_child(folium.Element(legend_html))


m.to_streamlit(height=700)
