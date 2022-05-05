# interview-exp-generator
Hi Guys, this is a python script to generate Interview Experiences from geeksforgeeks.org.
All you gotta do is to run fetchInterviewExperience.py file.  
It will automatically download all the interview experience for any company from
Geeks for geeks and then convert it to pdf and save it
To your local storage. 

## Scope of Modification
You can modify the list of companies to fetch their interview experience.  
I have added four companies but you can add/remove any company you want by changing the list ```companies```
```
companies = [company1_name, company2_name ..... companyn_name]
```
> Here companyN_name is the name of company in lower case and N is the total number of companies



# Requirements/Steps to Reproduce
You need to have a laptop/computer with python installed in it. 
Then you need to install below Libraries from PIP.
```
pip install httplib2
pip install bs4
pip install pdfkit
pip install PyPDF2
```
After installing all the libraries, you need to run the python script.
```
python fetchInterviewExperience.py
```
After running this script the fetching will start, it will fetch interview experiences of all the companies one by one and convert it to pdf  
Then it will merge all the PDFs of a particular company into one PDF and store it at below path
```
./InterviewExperiences/company_nameInterviewExperience.pdf
```

That's it folks !!  
You now have the interview experience of your desired company.  
Keep studying !!  
All the Best !!  

# Thank You
