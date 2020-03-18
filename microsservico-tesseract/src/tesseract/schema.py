import graphene
import ocr.schema


class Query(ocr.schema.Query, graphene.ObjectType):
    pass


class Mutation(ocr.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
