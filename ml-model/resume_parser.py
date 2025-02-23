#Resume Parsing Script

import spacy
import pdfplumber 
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from resume pdf"""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
    
def extract_details(text):
    """extract name, email, phone, and skills from resume text"""
    doc = nlp(text)

    #extract name
    name = doc.ents[0].text if doc.ents else "Not Found"

    #extract email
    email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    email = email.group() if email else "Not Found"

    #extract phone
    phone = re.search(r"\+?\d[\d -]{8,}\d", text) #number formats like +91 98765 43210, +1-800-555-0199, 999-888-777, 9876543210 etc
    phone = phone.group() if phone else "Not Found"

    #extract_skills
    skills_keywords = ["Python", "Machine Learning", "Deep Learning", "NLP", "Javascript", "React", "SQL"]
    skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]

    return{
        "name" : name,
        "email" : email,
        "phone" : phone,
        "skills" : skills
    }
     
