from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . import forms
from . import schema
from core import tesseract_pdf as t_pdf


def index(request):
    return HttpResponse('OCR Time')


class OcrView(View):
    def ocr(self, pdf_path):
        outputText = t_pdf.read_pdf_from_path(pdf_path)
        return outputText

    def uploadPdf(self, pdfFile):
        result = schema.execute(
            '''
            mutation uploadPdf ($pdfFile: Upload!) {
                uploadPdf(pdfFile: $pdfFile) {
                    newPdf {
                        id
                        pdfFile
                    }
                }
            }
            ''',
            variables={'$pdfFile': pdfFile}
        )
        return result

    def updatePdf(self, pdf_id, pdf_text):
        # TODO: Add latest_access & latest_user
        result = schema.execute(
            '''
            mutation updatePdf ($id: ID!, $text: String) {
                updatePdfText (text: $text) {
                    pdf {
                        id
                        pdfFile
                        text
                    }
                }
            }
            ''',
            variables={'$id': pdf_id, '$text': pdf_text}
        )
        return result

    def ocr_render(self, request):
        form = forms.UploadPdfForm()
        outputText = None

        if request.method == 'POST':
            form = forms.UploadPdfForm(request.POST, request.FILES)
            if form.is_valid():
                pdf_obj = form.save()
                outputText = self.ocr('uploads/' +
                                      request.FILES['pdf_file'].name)
                self.updatePdf(pdf_obj.id, outputText)
        else:
            form = forms.UploadPdfForm()

        context = {'form': form, 'outputText': outputText}
        return render(request, 'ocr/ocr.html', context)
