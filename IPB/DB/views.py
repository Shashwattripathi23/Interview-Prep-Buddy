from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader


from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader
import spacy


def generate(request):
    print(request.FILES)
    pdf_file = request.FILES.get('pdfFile')

    if request.method == 'POST' and pdf_file:
        # Check if the file is a PDF using content type
        if pdf_file.content_type != 'application/pdf':
            return HttpResponse('Invalid file format. Please upload a PDF file.')

        # Read the PDF content
        pdf_reader = PdfReader(pdf_file)

        # Extract text from all pages
        resume_text = ''
        for page in pdf_reader.pages:
            resume_text += page.extract_text()
            print(resume_text)

        # Load spaCy's English language model
        nlp = spacy.load(
            r"C:\Users\SHASHWAT\Desktop\Python\Django\IPB\IPB\Pymodel\27")

        # Process the resume text using spaCy
        doc = nlp(resume_text)

        # Extract entities (skills in this case)
        skills = [ent.text for ent in doc.ents if ent.label_ ==
                  'TECH_SKILL']

        # You can now use 'skills' in the further steps of your application

        # Example: Displaying extracted skills in the response
        return HttpResponse(f'Skills extracted from the resume: {", ".join(skills)}')

    # Replace 'your_template_name' with your actual template name
    return render(request, 'inp.html')
