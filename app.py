import streamlit as st
import os.path

st.set_page_config(
    page_title="PhysiSTEM AI • Học Vật lí KNTT 6–9",
    page_icon="⚛️",
    layout="wide"
)

# Ẩn header và footer mặc định của Streamlit
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0rem;
    }
</style>
""", unsafe_allow_html=True)

# Đọc và hiển thị tệp index.html gốc đã được tích hợp menu Trợ lý AI
html_file_path = "index.html"
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=1100, scrolling=True)
else:
    st.error("⚠️ Không tìm thấy tệp `index.html` trong thư mục `C:\\Users\\win 10\\Desktop\\stem\\`!")