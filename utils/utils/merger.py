import io
from pypdf import PdfWriter


def merge_pdfs(pdf_list):

    writer = PdfWriter()

    for pdf in pdf_list:
        writer.append(pdf)

    output = io.BytesIO()

    writer.write(output)

    output.seek(0)

    return output
