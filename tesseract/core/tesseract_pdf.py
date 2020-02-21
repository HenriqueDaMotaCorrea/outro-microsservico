import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def get_img_string(img):
    result = pytesseract.image_to_string(img, lang='por')
    return result


def pdf_to_img(pdf_path):
    pages = convert_from_path(pdf_path)
    return pages


def get_pdf_string(pages):
    text = ''
    for i in pages:
        page_text = get_img_string(i)
        text += page_text
    return text


def read_image_from_path(img_path):
    image = Image.open(img_path)
    return get_img_string(image)


def read_pdf_from_path(pdf_path):
    return get_pdf_string(pdf_to_img(pdf_path))
