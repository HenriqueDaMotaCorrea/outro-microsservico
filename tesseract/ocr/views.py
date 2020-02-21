from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from core import tesseract_pdf


def index(request):
    return HttpResponse('OCR Time')


def ocr(request):
    form = forms.UploadPdfForm()
    outputText = None
    if request.method == 'POST':
        form = forms.UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            outputText = tesseract_pdf.get_pdf_string()
        else:
            form = forms.UploadPdfForm()
    return render(request,
                  'ocr/ocr.html',
                  {'form': form, 'outputText': outputText})
