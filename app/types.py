import strawberry
from app.models import Card, List

@strawberry.type
class TableType:
    id: int
    title: str
    @strawberry.field
    def lists(self) -> list['ListType']:
        return List.objects.filter(table_id=self.id)

@strawberry.type
class ListType:
    id: int
    title: str
    table:TableType
    @strawberry.field
    def cards(self) -> list['CardType']:
        return Card.objects.filter(list_id=self.id)

@strawberry.type
class CardType:
    id: int
    title: str
    list:ListType
