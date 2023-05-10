from PyPDF2 import PdfReader
import chardet


def convert_to_rawtext(extension, file):
    # Get the file extension
    if extension == '.pdf':
        reader = PdfReader(file)
        text = ""
        for i in range(len(reader.pages)):
            text += reader.pages[i].extract_text()
        print(text)
        return text
    # Check if the file is a CSV
    elif extension == '.csv':
        result = chardet.detect(file)
        encoding = result['encoding']
        data = file.decode(encoding)
        print(data)

        return {'data': data}
    # If the file is neither a PDF nor a CSV
    else:
        print('Unsupported file type')
        return
