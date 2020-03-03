from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from core import tesseract_pdf as t_pdf


def index(request):
    return HttpResponse('OCR Time')


def ocr(request):
    form = forms.UploadPdfForm()
    outputText = None

    if request.method == 'POST':
        form = forms.UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            pdf_path = 'uploads/' + request.FILES['pdf_file'].name
            outputText = t_pdf.read_pdf_from_path(pdf_path)
    else:
        form = forms.UploadPdfForm()

    context = {'form': form, 'outputText': outputText}
    return render(request, 'ocr/ocr.html', context)
