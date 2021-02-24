import os, re
from PyPDF2 import PdfFileWriter, PdfFileReader
from tika import parser

# parameter variables
extract_to = r"C:\repositorio\split-pdf-rendimentos-dirf-by-cpf\rendimentos\extract"
rename_to = r"C:\repositorio\split-pdf-rendimentos-dirf-by-cpf\rendimentos\rename"
prefixo_file = 'IRRF2020_'
filename_all_rendimentos = 'comprovantes-ir-2020-dirf.pdf'

# constants variables
inputname_to_find = 'Nome Completo'
pdf_extension = '.pdf'



def split_pdf_pages():
    inputpdf = PdfFileReader(open(filename_all_rendimentos, "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)


def rename_pdfs(extraced_pdf_folder, rename_folder):
    for root, dirs, files in os.walk(extraced_pdf_folder):
        
        for filename in files:
            basename, extension = os.path.splitext(filename)
            
            if extension == pdf_extension:
                fullpath = root + "/" + basename + extension
                raw = parser.from_file(fullpath)
                raw = str(raw)
                safe_text = raw.encode('utf-8', errors='ignore')
                safe_text = str(safe_text).replace("\n", "").replace("\\", "")
                
                for index in re.finditer(inputname_to_find, safe_text):
                    doc_num = safe_text[index.end() + 2:index.end() + 16]
                    doc_num = prefixo_file + doc_num.replace('.', '').replace('-', '')
                    os.rename(fullpath, rename_folder + "/" + doc_num + pdf_extension)

split_pdf_pages()
rename_pdfs(extract_to, rename_to)
