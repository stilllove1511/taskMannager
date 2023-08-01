import strawberry
from app.schema.card import CardMutation, CardQuery

from app.schema.list import ListMutation, ListQuery
from app.schema.table import TableMutation, TableQuery

@strawberry.type
class Query(
    CardQuery,
    TableQuery,
    ListQuery,
):
    pass

@strawberry.type
class Mutation(
    CardMutation,
    TableMutation,
    ListMutation,
):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
