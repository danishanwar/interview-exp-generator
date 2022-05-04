from PyPDF2 import PdfFileMerger, PdfFileReader
merger = PdfFileMerger()
pdfs = ['amazon0.pdf','amazon1.pdf']
companies = ['google','qualcomm','amazon','microsoft']
z=3;
for file_name in pdfs:
    with open(file_name, 'rb') as f:
        merger.append(f, import_bookmarks=False )

merger.write('InterviewExperiences/'+companies[z]+'InterviewExperience'+'.pdf')