import pdfplumber
import docx
from datetime import datetime

today_date_time = datetime.now()
def get_pdf_text(document, from_path,to_path,page_from, page_to, document_extension='docx',):
    pdf = pdfplumber.open(path)
    numPages = len(pdf.pages)
    print(numPages)
    #Page Number validation 
    if 1 <= page_from <= page_to <= numPages:
        #iterate Each Page 
        print("Test", page_from, page_to, numPages)
        for page_number in range(page_from - 1, page_to):
            print("Page Number:", page_number + 1)
            page = pdf.pages[page_number]
            text = page.extract_text()
            print(text)
            #add pages to docx
            document.add_paragraph(text)
    #save all the pages 
    file_name = today_date_time.strftime("%H%M%S")
    document.save(f"{to_path}{file_name}.{document_extension}")
          
 
my_doc = docx.Document()
path = input("Enter Path of the file to extract text from: ")
path_to_save = 'D:\\'
get_pdf_text(my_doc,path,path_to_save,1,3,"docx")