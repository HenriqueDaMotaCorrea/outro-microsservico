from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . import forms
from core import tesseract_pdf as t_pdf


def index(request):
    return HttpResponse('OCR Time')


class OcrView(View):
    def ocr(self, pdf_path):
        outputText = t_pdf.read_pdf_from_path(pdf_path)
        return outputText

    def ocr_render(self, request):
        form = forms.UploadPdfForm()
        outputText = None

        if request.method == 'POST':
            form = forms.UploadPdfForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                outputText = self.ocr('uploads/' +
                                      request.FILES['pdf_file'].name)
        else:
            form = forms.UploadPdfForm()

        context = {'form': form, 'outputText': outputText}
        return render(request, 'ocr/ocr.html', context)
