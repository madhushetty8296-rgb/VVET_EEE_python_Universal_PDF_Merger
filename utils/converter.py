import io

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter

from docx import Document


def image_to_pdf(image_file):
    image = Image.open(image_file)

    if image.mode != "RGB":
        image = image.convert("RGB")

    pdf_bytes = io.BytesIO()

    c = canvas.Canvas(pdf_bytes, pagesize=letter)

    width, height = letter

    img_width, img_height = image.size

    ratio = min(width / img_width, height / img_height)

    new_width = img_width * ratio
    new_height = img_height * ratio

    x = (width - new_width) / 2
    y = (height - new_height) / 2

    c.drawImage(
        ImageReader(image),
        x,
        y,
        width=new_width,
        height=new_height
    )

    c.save()

    pdf_bytes.seek(0)

    return pdf_bytes


def docx_to_pdf(docx_file):

    document = Document(docx_file)

    pdf_bytes = io.BytesIO()

    c = canvas.Canvas(pdf_bytes)

    y = 800

    for para in document.paragraphs:

        c.drawString(40, y, para.text)

        y -= 20

        if y < 50:
            c.showPage()
            y = 800

    c.save()

    pdf_bytes.seek(0)

    return pdf_bytes
