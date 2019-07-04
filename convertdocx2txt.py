from docx import Document


def convertDocxToText(path):
	document = Document(path)
	return "\n".join([para.text for para in document.paragraphs])

print(convertDocxToText('''Path of the docx type file'''))