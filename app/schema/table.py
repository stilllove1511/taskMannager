# file: myapp/schema.py
import strawberry
from app.models import Table

from typing import List

from app.types import TableType



@strawberry.type
class TableQuery:
    @strawberry.field
    def getTable(self) -> List[TableType]:
        return Table.objects.all()
    @strawberry.field
    def getTableById(self, id: int) -> TableType:
        return Table.objects.get(id=id)

@strawberry.type
class TableMutation:
    @strawberry.mutation
    def addTable(self, title: str) -> TableType:
        return Table.objects.create(title=title)
    @strawberry.mutation
    def updateTable(self, id: int, title: str) -> TableType:
        return Table.objects.filter(id=id).update(title=title)
    @strawberry.mutation
    def deleteTable(self, id: int) -> TableType:
        return Table.objects.filter(id=id).delete()