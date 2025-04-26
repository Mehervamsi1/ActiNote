from docx import Document

file_path ="code\sample_meeting.docx"

def read_docx_transcript(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

#Testing

#print(read_docx_transcript(file_path))