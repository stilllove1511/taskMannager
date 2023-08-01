import strawberry
from ..models import List as ListModel, Card
from typing import List

@strawberry.type
class ListType:
    id: int
    title: str
@strawberry.type
class ListQuery:
    @strawberry.field
    def getList(self) ->List[ListType]:
        return ListModel.objects.all()
    @strawberry.field
    def getListById(self, id: int) -> ListType:
        return ListModel.objects.get(id=id)

@strawberry.type
class ListMutation:
    @strawberry.mutation
    def addList(self, title: str,) -> ListType:
        return ListModel.objects.create(title=title)
    @strawberry.mutation
    def updateList(self, id: int, title: str) -> ListType:
        return ListModel.objects.filter(id=id).update(title=title)
    @strawberry.mutation
    def deleteList(self, id: int) -> ListType:
        return ListModel.objects.filter(id=id).delete()
