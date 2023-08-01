# file: myapp/schema.py
import strawberry

from app.schema.list import ListType

from ..models import List as ListModel
from typing import List

@strawberry.type
class TableType:
    id: int
    title: str
    list: ListType

@strawberry.type
class TableQuery:
    @strawberry.field
    def getTable(self) -> List[TableType]:
        return ListModel.objects.all()
    @strawberry.field
    def getTableById(self, id: int) -> TableType:
        return ListModel.objects.get(id=id)

@strawberry.type
class TableMutation:
    @strawberry.mutation
    def addTable(self, title: str) -> TableType:
        return ListModel.objects.create(title=title)
    @strawberry.mutation
    def updateTable(self, id: int, title: str) -> TableType:
        return ListModel.objects.filter(id=id).update(title=title)
    @strawberry.mutation
    def deleteTable(self, id: int) -> TableType:
        return ListModel.objects.filter(id=id).delete()