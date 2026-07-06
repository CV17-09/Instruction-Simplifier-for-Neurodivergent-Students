import fitz
import docx

def extract_pdf_text(file_path: str) -> str:
    text = ""

    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()

    return text

def extract_docx_text(file_path: str) -> str:
    document = docx.Document(file_path)
    return "\n".join([paragraph.text for paragraph in document.paragraphs])

def clean_text(text: str) -> str:
    return " ".join(text.split())