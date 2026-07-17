import streamlit as st

from utils.converter import image_to_pdf
from utils.converter import docx_to_pdf
from utils.merger import merge_pdfs
from utils.viewer import display_pdf

st.set_page_config(
    page_title="Multi File PDF Merger",
    layout="wide"
)

st.title("📄 Multi File PDF Merger")

uploaded_files = st.file_uploader(
    "Upload Files",
    accept_multiple_files=True,
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "docx"
    ]
)

if uploaded_files:

    pdf_files = []

    for file in uploaded_files:

        suffix = file.name.split(".")[-1].lower()

        if suffix == "pdf":

            pdf_files.append(file)

        elif suffix in ["png", "jpg", "jpeg"]:

            pdf_files.append(image_to_pdf(file))

        elif suffix == "docx":

            pdf_files.append(docx_to_pdf(file))

    merged_pdf = merge_pdfs(pdf_files)

    st.success("Merge Complete!")

    st.download_button(
        "⬇ Download Merged PDF",
        merged_pdf,
        "merged.pdf",
        "application/pdf"
    )

    merged_pdf.seek(0)

    display_pdf(merged_pdf)
