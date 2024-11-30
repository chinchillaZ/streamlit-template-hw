import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("結合Sentinel影像與機器學習分群技術分析水稻田倒伏模式")

st.markdown(
    """
    本研究以2024年台東地區接連受凱米、山陀兒與康瑞颱風侵襲所造成的水稻田倒伏現象為背景，選定池上、鹿野與關山為研究區域，結合Sentinel-1與Sentinel-2衛星影像進行分析。透過提取NDVI等植生指數及地表特徵，應用機器學習分群技術（如K-means與DBSCAN）辨識倒伏區域特性。研究結果顯示，分群方法能有效提供倒伏分布模式與災害影響範圍的空間資訊，為災後農損評估與防災策略制定提供重要參考。
    """
)

st.header("研究區域")

markdown = """
選定池上、關山與鹿野為研究區域，原因在於:
三地位於花東縱谷平原內，空間相鄰且稻田面積連續且廣大，適合作為觀測倒伏模式的樣本範圍，
有助於分析颱風災害對水稻田的影響。
"""

st.markdown(markdown)

m = leafmap.Map(center=[23.1, 121.2], zoom=10,minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
