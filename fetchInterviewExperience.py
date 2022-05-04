# Copyright @ MD Danish Anwar
# Version 1.1
# Follow @ GitHub :- https://github.com/danishanwar
# Follow @ LinkedIn :- https://www.linkedin.com/in/iammda23/


# This is a python script to fetch interview experience of any company from geeks for geeks
# in the form of PDF
# All one needs to do is to fill the list companies[] with the name of companies whose experience
# you want and then run the script
# Here in this script, I am fetching interview experience for Amazon, Google, Microsoft and Qualcomm.
# You can add or remove any company name in the list companies[] and get desired output.

import httplib2
import pdfcrowd
from bs4 import BeautifulSoup, SoupStrainer
import pdfkit
import sys

#Preparing the link for each company
tagLink = 'https://www.geeksforgeeks.org/tag/'
remLink = '/page/'
http = httplib2.Http()

#List of companies
companies = ['google','qualcomm','amazon','microsoft']
i=0

#Function to get number of pages for a particular company

def getNumberOfPages(sourceUrl):
    status, response = http.request(sourceUrl)
    soup = BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a'))
    last = soup.find(class_="last")
    if last.has_attr('href'):
        li=last['href']
    sli = li.split('/')
    numPages = sli[-2]
    a = int(numPages)
    return a

#This loop will run for each company i.e. number of times this loop will run is same
#as number of companies.
#For each company this loop will generate a file called company_nameInterviewExperience.pdf

for z in range(len(companies)):
    t = tagLink+companies[z]+remLink
    s = t+'1'
    #print(s)
    to_crawl=[]
    i=0
    numPages = getNumberOfPages(s);
    for j in range(numPages):
        s=t+str(j+1)
        #print(s)
        status, response = http.request(s)
        mycount = 0

        #For every page of a company's interview experience, we'll fetch all the links from that page
        for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
                #print(link)
                if link.has_attr('href'):
                    li=link['href']
                    mycount+=1
                    to_crawl.append(li)


                 
        listofAllLinks=[ ]
        
        # Here for all the links in that page, we'll check if that link has company's name in it.
        #If yes we'll append it to our final list.
        for st in to_crawl:
            #print(st)
            if st.find(companies[z])>=0 and st.find('#')<0 and st.find('tag')<0 and st.find('forum')<0:
                #print("string is " + st)
                listofAllLinks.append(st)


    k=0

    listOfLink = []
    for k in range(len(listofAllLinks)):
        if k%2==0:
            listOfLink.append(listofAllLinks[k])

    # This List listofLink will have all the links of every interview experience of 
    # a particular company.
    # We can then go to every page and convert the HTML to PDF 
    # and at last merge all the PDFs
    print(len(listOfLink))



    count=0
    pdfs = [ ]

    # Function to save HTML content of a page as PDF
    def save_as_pdf(s):
        global i
        output_file = open(companies[z]+str(i)+'.pdf', 'wb')
        print(output_file.name)
        pdfs.append(output_file.name)
        i=i+1
        status, response = http.request(s)
        soup = BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('article'))
        print(s)
        original_stdout = sys.stdout # Save a reference to the original standard output

        with open('temp'+companies[z]+str(i)+'.html', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print('<html><body>')
            print('<style>body {background-color: #fcf;color:#black; font-size:20px;font-family:Helvetica;}</style>')
            #print(soup)
            print(soup.encode("utf-8"))
            print('</html></body>')
            sys.stdout = original_stdout

        pdfkit.from_file('temp'+companies[z]+str(i)+'.html', output_file.name)
        output_file.close()

    # Converting every HTML Page containing interview experience to PDF
    for item in listOfLink:
        save_as_pdf(item)
        #print(item)

    # print(pdfs)

    # Merging all the PDFs of a particular company into one Final PDF.
    from PyPDF2 import PdfFileMerger, PdfFileReader
    merger = PdfFileMerger()
    for file_name in pdfs:
        with open(file_name, 'rb') as f:
            merger.append(f, import_bookmarks=False )

    merger.write('InterviewExperiences/'+companies[z]+'InterviewExperience'+'.pdf')