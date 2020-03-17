import graphene
from graphene_django.types import DjangoObjectType
from ocr.models import Pdf


class PdfType(DjangoObjectType):
    class Meta:
        model = Pdf


class Query(object):
    all_pdfs = graphene.List(PdfType)
    pdf = graphene.Field(PdfType,
                         id=graphene.Int(),
                         pdf_file=graphene.String(),
                         text=graphene.String())

    def resolve_all_pdfs(self, info, **kwargs):
        return Pdf.objects.all()

    def resolve_pdf(self, info, **kwargs):
        id = kwargs.get('id')
        pdf_file = kwargs.get('pdf_file')
        text = kwargs.get('text')

        if id is not None:
            return Pdf.objects.get(pk=id)

        if pdf_file is not None:
            return Pdf.objects.get(pk=pdf_file)

        if text is not None:
            return Pdf.objects.get(pk=text)

        return None
