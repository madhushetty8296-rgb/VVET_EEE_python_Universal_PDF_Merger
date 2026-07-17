import fitz
import streamlit as st


def display_pdf(pdf_bytes):

    pdf = fitz.open(stream=pdf_bytes.read(), filetype="pdf")

    st.subheader("Merged PDF Preview")

    for page_num in range(len(pdf)):

        page = pdf.load_page(page_num)

        pix = page.get_pixmap(dpi=150)

        image = pix.tobytes("png")

        st.image(
            image,
            caption=f"Page {page_num+1}",
            use_container_width=True
        )

    pdf.close()

    pdf_bytes.seek(0)
