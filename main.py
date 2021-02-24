import os, re
from PyPDF2 import PdfFileWriter, PdfFileReader
from tika import parser

# parameter variables
extract_to = r"C:\repositorio\split-pdf-rendimentos-dirf-by-cpf\rendimentos\extract"
rename_to = r"C:\repositorio\split-pdf-rendimentos-dirf-by-cpf\rendimentos\rename"
prefixo_file = 'IRRF2020_'



def split_pdf_pages():
    inputpdf = PdfFileReader(open("comprovantes-ir-2020-dirf.pdf", "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)


def rename_pdfs(extraced_pdf_folder, rename_folder):
    for root, dirs, files in os.walk(extraced_pdf_folder):
        
        for filename in files:
            basename, extension = os.path.splitext(filename)
            
            if extension == ".pdf":
                fullpath = root + "/" + basename + extension
                raw = parser.from_file(fullpath, 'http://localhost:9998/tika')
                raw = str(raw)
                safe_text = raw.encode('utf-8', errors='ignore')
                safe_text = str(safe_text).replace("\n", "").replace("\\", "")
                
                for index in re.finditer("Nome Completo", safe_text):
                    doc_num = safe_text[index.end() + 2:index.end() + 16]
                    doc_num = '{}{}'.format(prefixo_file, doc_num.replace('.', '').replace('-', ''))
                    os.rename(fullpath, rename_folder + "/" + doc_num + ".pdf")

split_pdf_pages()
rename_pdfs(extract_to,rename_to)
