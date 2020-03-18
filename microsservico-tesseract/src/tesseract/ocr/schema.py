import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload
from .models import Pdf


class PdfType(DjangoObjectType):
    class Meta:
        model = Pdf


class Query(object):
    all_pdfs = graphene.List(PdfType)
    pdf = graphene.Field(PdfType,
                         id=graphene.Int(),
                         pdf_file=graphene.String(),
                         text=graphene.String(),
                         latest_access=graphene.DateTime(),
                         latest_user=graphene.String())

    def resolve_all_pdfs(self, info, **kwargs):
        return Pdf.objects.all()

    def resolve_pdf(self, info, **kwargs):
        id = kwargs.get('id')
        pdf_file = kwargs.get('pdf_file')
        text = kwargs.get('text')
        latest_access = kwargs.get('latest_access')
        latest_user = kwargs.get('latest_user')

        if id is not None:
            return Pdf.objects.get(pk=id)

        if pdf_file is not None:
            return Pdf.objects.get(pk=pdf_file)

        if text is not None:
            return Pdf.objects.get(pk=text)

        if latest_access is not None:
            return Pdf.objects.get(pk=latest_access)

        if latest_user is not None:
            return Pdf.objects.get(pk=latest_user)

        return None


class CreatePdf(graphene.Mutation):
    class Arguments:
        pdf_file = Upload(required=True)

    new_pdf = graphene.Field(PdfType)

    def mutate(self, info, pdf_file, **kwargs):
        new_pdf = Pdf.objects.create(pdf_file=pdf_file)
        return CreatePdf(new_pdf=new_pdf)


class UpdatePdf(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        text = graphene.String(required=True)
        latestAccess = graphene.DateTime(required=True)
        latestUser = graphene.String(required=True)

    pdf = graphene.Field(PdfType)

    def mutate(self, info, id, text, latestAccess, latestUser):
        pdf = Pdf.objects.get(pk=id)
        pdf.text = text
        pdf.latest_access = latestAccess
        pdf.latest_user = latestUser
        pdf.save()
        return UpdatePdf(pdf=pdf)


class Mutation(graphene.ObjectType):
    upload_pdf = CreatePdf.Field()
    update_pdf = UpdatePdf.Field()
