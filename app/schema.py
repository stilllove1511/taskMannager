# file: myapp/schema.py
import strawberry
from .models import List as ListModel, Card
from typing import List

@strawberry.type
class ListType:
    title: str

@strawberry.type
class CardType:
    title: str
    list: int

@strawberry.type
class Query:
    @strawberry.field
    def getList(self) ->List[ListType]:
        return ListModel.objects.all()
    @strawberry.field
    def getListById(self, id: int) -> ListType:
        return ListModel.objects.get(id=id)
    @strawberry.field
    def getListByTitle(self, title: str) -> ListType:
        return ListModel.objects.get(title=title)
    @strawberry.field
    def getCard (self) -> List[CardType]:
        return Card.objects.all()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def addList(self, title: str,) -> ListType:
        return ListModel.objects.create(title=title)
    @strawberry.mutation
    def updateList(self, id: int, title: str) -> ListType:
        return ListModel.objects.filter(id=id).update(title=title)
    @strawberry.mutation
    def deleteList(self, id: int) -> ListType:
        return ListModel.objects.filter(id=id).delete()
    @strawberry.mutation
    def addCard(self, title: str, list: int) -> CardType:
        return Card.objects.create(title=title, list=list)
    @strawberry.mutation
    def updateCard(self, id: int, title: str, list: int) -> CardType:
        return Card.objects.filter(id=id).update(title=title, list_=list)
    @strawberry.mutation
    def deleteCard(self, id: int) -> CardType:
        return Card.objects.filter(id=id).delete()

schema = strawberry.Schema(query=Query, mutation=Mutation)
