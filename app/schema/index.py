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

# from ..models import List as ListModel, Card
# from typing import List

# @strawberry.type
# class ListType:
#     id: int
#     title: str

# @strawberry.type
# class ListQuery:
#     @strawberry.field
#     def getList(self) ->List[ListType]:
#         return ListModel.objects.all()
#     @strawberry.field
#     def getListById(self, id: int) -> ListType:
#         return ListModel.objects.get(id=id)

# @strawberry.type
# class ListMutation:
#     @strawberry.mutation
#     def addList(self, title: str) -> ListType:
#         return ListModel.objects.create(title=title)
#     @strawberry.mutation
#     def updateList(self, id: int, title: str) -> ListType:
#         return ListModel.objects.filter(id=id).update(title=title)
#     @strawberry.mutation
#     def deleteList(self, id: int) -> ListType:
#         return ListModel.objects.filter(id=id).delete()
    
# @strawberry.type
# class Query(
#     ListQuery,
# ):
#     pass

# @strawberry.type
# class Mutation(
#     ListMutation,
# ):
#     pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
