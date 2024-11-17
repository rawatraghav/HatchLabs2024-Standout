# resume_parser.py
import PyPDF2

class ResumeParser:
    def parse_resume(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return self.structure_resume_data(text)